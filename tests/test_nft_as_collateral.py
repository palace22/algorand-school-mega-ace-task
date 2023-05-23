from tests import *
from tests.helpers import *
from tests.fixtures import *
from contracts.nft_as_collateral import *


@pytest.mark.deploy
def test_deploy(algod_client: AlgodClient):
    user = generate_funded_account(algod_client)

    client = ApplicationClient(algod_client, nft_as_collateral_app, signer=user.signer, sender=user.address)
    app_id, _, _ = client.create()
    print("NFT Lending app id: {}".format(app_id))
    assert app_id != 0
