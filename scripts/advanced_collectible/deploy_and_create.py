from scripts.helpful_scripts import fund_with_link, get_account, get_contract
from brownie import AdvancedCollectible, config, network

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
    )
    fund_with_link(advanced_collectible.address)
    token_id = advanced_collectible.getTokenId()
    print(f"token_Id: {token_id}")
    tx = advanced_collectible.createCollectible({"from": account})
    tx.wait(1)

    latest_token_id = advanced_collectible.getTokenId()
    print(f"latest_token_id: {latest_token_id}")
    return advanced_collectible, tx


def main():
    deploy_and_create()
