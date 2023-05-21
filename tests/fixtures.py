from tests import *
from tests.helpers import *
from contracts.nft_lending import *

@pytest.fixture(scope="function")
def nft_lending_app_id(algod_client: AlgodClient):
    user = generate_funded_account(algod_client)
    client = ApplicationClient(algod_client, nft_lending_app, signer=user.signer, sender=user.address)
    app_id, app_addr, _ = client.create()
    algo_faucet(algod_client, app_addr)
    return app_id

