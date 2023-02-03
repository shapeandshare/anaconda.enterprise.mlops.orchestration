from typing import Optional

from anaconda.enterprise.server.contracts import BaseModel
from anaconda.enterprise.server.sdk import ClientOptions


class ConfigProperty(BaseModel):
    name: str
    value: str


class CloudFormationConfig(BaseModel):
    index: int
    file: str
    parameters: list[ConfigProperty]


class AwsConfig(BaseModel):
    region: str
    cloudformation: list[CloudFormationConfig]


class AnacondaEnterpriseServerConfig(BaseModel):
    options: ClientOptions


class AnacondaConfig(BaseModel):
    enterprise: AnacondaEnterpriseServerConfig


class MLFlowTrackingServerAEConfig(BaseModel):
    template_path: str
    project_name: str
    deployment_name: str
    static_endpoint_name: str


class MLFlowConfig(BaseModel):
    server: MLFlowTrackingServerAEConfig
    mlflow: list[ConfigProperty]


class Manifest(BaseModel):
    name: str
    aws: Optional[AwsConfig] = None
    anaconda: AnacondaConfig
    config: MLFlowConfig
