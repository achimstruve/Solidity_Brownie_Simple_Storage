from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    # get local ganache accout
    # account = accounts[0]

    # Get own MetaMask account with private key. Get all created accounts by typing "brownie accounts list".
    # Create a new accounts by "brownie accounts new <account_name>".
    # Delete an account by typing "brownie accounts delete <account_name>"
    # account = accounts.load("own-account")
    # print(account)

    # Get own MetaMask account with private key from environmental variables
    # account = accounts.add(os.getenv("PRIVATE_KEY")) # version 1
    # account = accounts.add(config["wallets"]["from_key"])  # version 2
    # print(account)

    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(
        1
    )  # waiting for one block to be mined that inlcudes the transaction
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()
