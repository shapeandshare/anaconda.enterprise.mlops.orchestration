from typing import Optional, Union

from anaconda.enterprise.server.contracts import (
    AERecordProjectResourceProfileType,
    BaseModel,
    JobCreateResponse,
    ProjectDeployResponse,
    ProjectRevision,
    ProjectUploadResponse,
)
from anaconda.enterprise.server.sdk import ClientOptions


class ConfigProperty(BaseModel):
    name: str
    value: str


class ExportProperty(BaseModel):
    name: str
    reference: str


class CloudFormationConfig(BaseModel):
    index: int
    file: str
    parameters: list[ConfigProperty]


class AwsConfig(BaseModel):
    region: str
    cloudformation: list[CloudFormationConfig]


class JobConfig(BaseModel):
    name: str
    command: str
    schedule: str
    autorun: bool = False
    variables: dict[str, str] = {}
    resource_profile: Optional[Union[AERecordProjectResourceProfileType, str]] = None


class DeploymentConfig(BaseModel):
    name: str
    command: str
    endpoint: Optional[str] = None
    resource_profile: Optional[Union[AERecordProjectResourceProfileType, str]] = None


class AEProjectConfig(BaseModel):
    index: int
    template_path: str
    project_name: str
    deployments: list[DeploymentConfig] = []
    exports: list[ExportProperty] = []
    jobs: list[JobConfig] = []


class AnacondaEnterpriseServerConfig(BaseModel):
    options: ClientOptions
    secrets: list[ConfigProperty]
    collection: list[AEProjectConfig]


class AnacondaConfig(BaseModel):
    enterprise: AnacondaEnterpriseServerConfig


class Manifest(BaseModel):
    name: str
    aws: Optional[AwsConfig] = None
    anaconda: AnacondaConfig


class ProjectDeploymentDetail(BaseModel):
    response: ProjectDeployResponse
    access_token: Optional[str] = None
    service_endpoint: Optional[str] = None


class ProjectLog(BaseModel):
    upload: Optional[ProjectUploadResponse] = None
    revisions: list[ProjectRevision] = []
    deployments: list[ProjectDeploymentDetail] = []
    exports: list[ConfigProperty] = []
    jobs: list[JobCreateResponse] = []
