import time
from pathlib import Path

from anaconda.enterprise.server.contracts import (
    BaseModel,
    ProjectDeployResponse,
    ProjectRevision,
    ProjectUploadResponse,
)
from anaconda.enterprise.server.sdk import AEClient

from ..utils import get_ae_client
from .dto.manifest import Manifest


class MLFlowInstaller(BaseModel):
    manifest: Manifest
    ae_client: AEClient

    def set_initial_ae_secrets(self) -> None:
        # Define our secrets

        # Remove possibly pre-existing configurations
        for mlflow_property in self.manifest.config.mlflow:
            key: str = mlflow_property.name
            try:
                self.ae_client.secret_delete(key=key)
            except Exception as error:
                # This is broad to allow for catching and reporting everything.
                print(error)

            # [re]create the secrets using the latest values.
            value: str = mlflow_property.value

            print(f"{key}:{value}")
            self.ae_client.secret_put(key=key, value=value)

    def set_final_ae_secrets(self, service_endpoint: str, access_token: str) -> None:
        # Define our secrets
        secrets: dict[str, str] = {
            "MLFLOW_TRACKING_URI": service_endpoint,
            "MLFLOW_REGISTRY_URI": service_endpoint,
            "MLFLOW_TRACKING_TOKEN": access_token,
        }

        print("The below values MUST bew provided to clients who wish to access the server and it's API.")
        print(
            "Please note that since this is a private deployment that a new token MUST be provided each time the server is restarted."
        )

        # [Re]create the secrets using the latest values.
        for key, value in secrets.items():
            print(f"{key}:{value}")
            self.ae_client.secret_delete(key=key)
            self.ae_client.secret_put(key=key, value=value)

    def upload_project(self) -> tuple[ProjectUploadResponse, list[ProjectRevision]]:
        upload_response: ProjectUploadResponse = self.ae_client.project_upload(
            project_archive_path=Path(self.manifest.config.server.template_path).resolve().as_posix(),
            name=self.manifest.config.server.project_name,
        )

        # Ensure the upload creation process has completed.
        project_revisions: list[ProjectRevision] = []
        retries: int = 10
        wait: bool = True
        while wait:
            project_revisions = self.ae_client.project_revisions_get(project_id=upload_response.id)
            if len(project_revisions) < 1:
                time.sleep(1)
                retries -= 1
            else:
                wait = False
            if retries <= 0:
                wait = False
        if retries <= 0:
            raise Exception("Retries count exceeded waiting for project upload to complete")

        return upload_response, project_revisions

    def create_deployment(self, project_id: str, revision_id: str) -> ProjectDeployResponse:
        deploy_params: dict = {
            "project_id": project_id,
            "deployment_name": self.manifest.config.server.deployment_name,
            "revision_id": revision_id,
            "command": "TrackingServer",
            "static_endpoint": self.manifest.config.server.static_endpoint_name,
        }
        return self.ae_client.project_deploy(**deploy_params)

    def deploy(self):
        self.set_initial_ae_secrets()
        project_upload_response, project_revisions = self.upload_project()
        project_deploy_response: ProjectDeployResponse = self.create_deployment(
            project_id=project_upload_response.id, revision_id=project_revisions[0].id
        )

        access_token: str = self.ae_client.deployment_token_get(deployment_id=project_deploy_response.id)
        service_endpoint: str = project_deploy_response.url
        self.set_final_ae_secrets(service_endpoint=service_endpoint, access_token=access_token)

        # job_creation_command: str = f"ae5 job create --command 'GarbageCollection' --schedule '*/10 * * * *' --name 'Scheduled {SERVER_PROJECT_NAME} Garbage Collection' '{SERVER_PROJECT_NAME}'"


if __name__ == "__main__":
    # Load configuration
    manifest_path: str = "mlflow/aws/environments/burt.mlflow.demo.json"
    manifest: Manifest = Manifest.parse_file(manifest_path)

    # Generate AE Client
    ae_client: AEClient = get_ae_client(options=manifest.anaconda.enterprise.options)

    # Create installer
    installer: MLFlowInstaller = MLFlowInstaller(manifest=manifest, ae_client=ae_client)

    # Install the application
    installer.deploy()
