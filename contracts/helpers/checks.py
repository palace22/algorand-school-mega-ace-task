from pyteal import *


def close_reminder_and_rekey_check():
    return Seq(
        Assert(Txn.close_remainder_to() == Global.zero_address()),
        Assert(Txn.rekey_to() == Global.zero_address()),
    )


def close_reminder_asset_close_and_rekey_check_of(txn: TxnObject):
    return Seq(
        Assert(txn.asset_close_to() == Global.zero_address()),
        Assert(txn.close_remainder_to() == Global.zero_address()),
        Assert(txn.rekey_to() == Global.zero_address()),
    )
