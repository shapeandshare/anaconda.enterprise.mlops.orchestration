from typing import Optional, Union

from anaconda.enterprise.server.contracts import (
    BaseModel,
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


class AEProjectConfigBase(BaseModel):
    index: int
    template_path: str
    project_name: str
    exports: list[ExportProperty] = []


class AEProjectConfig(AEProjectConfigBase):
    deployment_name: str
    static_endpoint_name: str


class AnacondaEnterpriseServerConfig(BaseModel):
    options: ClientOptions
    secrets: list[ConfigProperty]
    collection: list[Union[AEProjectConfig, AEProjectConfigBase]]


class AnacondaConfig(BaseModel):
    enterprise: AnacondaEnterpriseServerConfig


class Manifest(BaseModel):
    name: str
    aws: Optional[AwsConfig] = None
    anaconda: AnacondaConfig


class ProjectLog(BaseModel):
    upload: Optional[ProjectUploadResponse] = None
    revisions: list[ProjectRevision] = []
    deploy: Optional[ProjectDeployResponse] = None
    access_token: Optional[str] = None
    service_endpoint: Optional[str] = None
    exports: list[ConfigProperty] = []
