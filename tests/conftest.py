from tests import *


@pytest.fixture(scope="session")
def algod_client() -> AlgodClient:
    return sandbox.get_algod_client()
