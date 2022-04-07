from scripts.helpful_scripts import fund_with_link, get_account
from brownie import AdvancedCollectible, web3
from web3 import Web3


def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address, amount=Web3.toWei(0.1, "ether"))
    print(f"contract address:{advanced_collectible.address}")
    token_id = advanced_collectible.getTokenId()
    print(f"token_Id: {token_id}")

    tx = advanced_collectible.createCollectible({"from": account})
    tx.wait(1)

    latest_token_id = advanced_collectible.getTokenId()
    print(f"latest_token_id: {latest_token_id}")
