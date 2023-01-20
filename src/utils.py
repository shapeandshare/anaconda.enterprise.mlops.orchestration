""" Notebook Helpers """

from typing import Optional

from anaconda.enterprise.server.common.sdk import demand_env_var
from anaconda.enterprise.server.sdk.client import AEClient
from anaconda.enterprise.server.sdk.contract.dto.client_options import ClientOptions
from anaconda.enterprise.server.sdk.session.factory import AESessionFactory


def get_ae_client(options: Optional[ClientOptions] = None) -> AEClient:
    """
    Get an AE Client

    Parameters
    ----------
    options: Optional[ClientOptions]
        Optional configuration for the client instantiation.

    Returns
    -------
    client: AEClient
        An instance of an AEClient.
    """

    if options is None:
        options_dict: dict = {
            "hostname": demand_env_var(name="AE_HOSTNAME"),
            "username": demand_env_var(name="AE_USERNAME"),
            "password": demand_env_var(name="AE_PASSWORD"),
        }
        options: ClientOptions = ClientOptions.parse_obj(options_dict)

    session_factory: AESessionFactory = AESessionFactory(options=options)
    return AEClient(session_factory=session_factory)
