from pyteal import *


def send_asset_transfer_transaction(asa_id: Expr, receiver: Expr, amount: Expr):
    return Seq(
        InnerTxnBuilder.Execute(
            {
                TxnField.type_enum: TxnType.AssetTransfer,
                TxnField.xfer_asset: asa_id,
                TxnField.asset_receiver: receiver,
                TxnField.asset_amount: amount,
                TxnField.fee: Int(0),
            }
        )
    )


def send_opt_in_transaction(asa_id: Expr):
    return Seq(
        InnerTxnBuilder.Execute(
            {
                TxnField.type_enum: TxnType.AssetTransfer,
                TxnField.xfer_asset: asa_id,
                TxnField.asset_receiver: Global.current_application_address(),
                TxnField.asset_amount: Int(0),
                TxnField.fee: Int(0),
            }
        )
    )
