from anaconda.enterprise.server.contracts import BaseModel
from anaconda.enterprise.server.sdk import ClientOptions


class AnacondaEnterpriseServerConfig(BaseModel):
    options: ClientOptions


class AnacondaConfig(BaseModel):
    enterprise: AnacondaEnterpriseServerConfig


class MLFlowTrackingServerAEConfig(BaseModel):
    template_path: str
    project_name: str
    deployment_name: str
    static_endpoint_name: str


class ConfigProperty(BaseModel):
    name: str
    value: str


class MLFlowConfig(BaseModel):
    server: MLFlowTrackingServerAEConfig
    mlflow: list[ConfigProperty]


class Manifest(BaseModel):
    name: str
    region: str
    anaconda: AnacondaConfig
    config: MLFlowConfig
