from pyteal import *
from beaker import *
from contracts.helpers.checks import *
from contracts.helpers.inners import *


class State:
    collateral_id = LocalStateValue(stack_type=TealType.uint64)
    borrowing_id = LocalStateValue(stack_type=TealType.uint64)
    amount = LocalStateValue(stack_type=TealType.uint64)
    duration = LocalStateValue(stack_type=TealType.uint64)
    interest = LocalStateValue(stack_type=TealType.uint64)  # 2 d.p.

    start = LocalStateValue(stack_type=TealType.uint64)
    lender = LocalStateValue(stack_type=TealType.bytes)


nft_as_collateral_app = Application("NFTasCollateral", state=State)


@nft_as_collateral_app.external
def opt_in_nft():
    return Approve()


@nft_as_collateral_app.opt_in(bare=True)
def opt_in_borrower():
    return Approve()


# Borrower
@nft_as_collateral_app.external
def request_loan():
    return Approve()


@nft_as_collateral_app.external
def delete_request():
    return Approve()


@nft_as_collateral_app.external
def repay_loan():
    return Approve()


# Lender
@nft_as_collateral_app.external
def accept_loan():
    return Approve()


@nft_as_collateral_app.external
def liquidate_loan():
    return Approve()
