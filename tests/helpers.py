from tests import *
from algosdk.account import generate_account


def generate_funded_account(algod_client: AlgodClient, amt=10_000_000):
    sandbox_faucet = sandbox.get_accounts().pop()
    private_key, address = generate_account()
    txn = PaymentTxn(sandbox_faucet.address, algod_client.suggested_params(), address, amt)
    algod_client.send_transaction(txn.sign(sandbox_faucet.private_key))
    return SandboxAccount(address=address, private_key=private_key)


def algo_faucet(algod_client: AlgodClient, address: str, amt=10_000_000):
    sandbox_faucet = sandbox.get_accounts().pop()
    txn = PaymentTxn(sandbox_faucet.address, algod_client.suggested_params(), address, amt)
    return algod_client.send_transaction(txn.sign(sandbox_faucet.private_key))


def create_asset(algod_client: AlgodClient, creator: SandboxAccount, total: int = 2**64 - 1, decimals: int = 6):
    txn = AssetCreateTxn(creator.address, algod_client.suggested_params(), total, decimals, False)
    tx_id = algod_client.send_transaction(txn.sign(creator.private_key))
    return algod_client.pending_transaction_info(tx_id)["asset-index"]


def create_nft(algod_client: AlgodClient, creator: SandboxAccount):
    return create_asset(algod_client, creator, 1, 0)


def asset_transfer(algod_client: AlgodClient, sender: SandboxAccount, receiver: str, asa_id: int, amt: int):
    txn = AssetTransferTxn(sender.address, algod_client.suggested_params(), receiver, amt, asa_id)
    return algod_client.send_transaction(txn.sign(sender.private_key))


def opt_in_asset(algod_client: AlgodClient, account: SandboxAccount, asa_id: int):
    txn = AssetOptInTxn(account.address, algod_client.suggested_params(), asa_id)
    return algod_client.send_transaction(txn.sign(account.private_key))
