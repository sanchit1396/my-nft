from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    token_id = simple_collectible.getTokenId()
    print(f"token_Id: {token_id}")
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(f"transaction{tx}")
    latest_token_id = simple_collectible.getTokenId()
    print(f"latest_token_id: {latest_token_id}")

    print(
        f"You can view your NFT at {OPENSEA_URL.format(simple_collectible.address, latest_token_id)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button. ")
    return simple_collectible


def main():
    deploy_and_create()
