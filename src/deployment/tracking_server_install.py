import time
from pathlib import Path
from typing import Optional, Union

from anaconda.enterprise.server.contracts import (
    BaseModel,
    ProjectDeployResponse,
    ProjectRevision,
    ProjectUploadResponse,
)
from anaconda.enterprise.server.sdk import AEClient

from ..utils import get_ae_client
from .dto.manifest import AEProjectConfig, AEProjectConfigBase, ConfigProperty, Manifest, ProjectLog


class MLFlowInstaller(BaseModel):
    manifest: Manifest
    ae_client: AEClient

    def set_secrets(self, secrets: list[ConfigProperty]) -> None:
        # Define our secrets

        # Remove possibly pre-existing configurations
        for secret in secrets:
            key: str = secret.name
            try:
                self.ae_client.secret_delete(key=key)
            except Exception as error:
                # This is broad to allow for catching and reporting everything.
                print(error)

            # [re]create the secrets using the latest values.
            value: str = secret.value

            print(f"{key}:{value}")
            self.ae_client.secret_put(key=key, value=value)

    def upload_project(
        self, project_archive_path: str, project_name: str
    ) -> tuple[ProjectUploadResponse, list[ProjectRevision]]:
        upload_response: ProjectUploadResponse = self.ae_client.project_upload(
            project_archive_path=Path(project_archive_path).resolve().as_posix(),
            name=project_name,
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

    def create_deployment(self, project: AEProjectConfig, project_id: str, revision_id: str) -> ProjectDeployResponse:
        deploy_params: dict = {
            "project_id": project_id,
            "deployment_name": project.deployment_name,
            "revision_id": revision_id,
            "command": "TrackingServer",
            "static_endpoint": project.static_endpoint_name,
        }
        return self.ae_client.project_deploy(**deploy_params)

    @staticmethod
    def get_value_from_reference(reference: str, log: ProjectLog) -> Optional[str]:
        # TODO: Make this leverage the reference as a namespace so this works generically..
        if reference == "log.service_endpoint":
            return log.service_endpoint
        if reference == "log.access_token":
            return log.access_token

    def deploy(self) -> list[ProjectLog]:
        # Set Pre-Install Configuration Parameters
        self.set_secrets(secrets=self.manifest.anaconda.enterprise.secrets)

        sorted_collection: list[Union[AEProjectConfig, AEProjectConfigBase]] = sorted(
            self.manifest.anaconda.enterprise.collection, key=lambda x: x.index
        )

        collection_log: list[ProjectLog] = []
        for project in sorted_collection:
            project_log: ProjectLog = ProjectLog()
            project_upload_response, project_revisions = self.upload_project(
                project_archive_path=project.template_path,
                project_name=project.project_name,
            )
            project_log.upload = project_upload_response
            project_log.revisions = project_revisions

            if hasattr(project, "deployment_name") and project.deployment_name is not None:
                # Create Deployment
                project_deploy_response: ProjectDeployResponse = self.create_deployment(
                    project=project, project_id=project_upload_response.id, revision_id=project_revisions[0].id
                )

                # Retrieve Runtime Configuration Of Deployment
                access_token: str = self.ae_client.deployment_token_get(deployment_id=project_deploy_response.id)
                service_endpoint: str = project_deploy_response.url

                project_log.deploy = project_deploy_response
                project_log.access_token = access_token
                project_log.service_endpoint = service_endpoint

                # Export Values
                if len(project.exports) > 0:
                    secrets: list[ConfigProperty] = []
                    for export in project.exports:
                        new_config: ConfigProperty = ConfigProperty(
                            name=export.name,
                            value=MLFlowInstaller.get_value_from_reference(reference=export.reference, log=project_log),
                        )
                        secrets.append(new_config)
                    self.set_secrets(secrets=secrets)
            collection_log.append(project_log)
        return collection_log

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
    log: list[ProjectLog] = installer.deploy()
    print(log)
