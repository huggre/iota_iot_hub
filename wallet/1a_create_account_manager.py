# Copyright 2020 IOTA Stiftung
# SPDX-License-Identifier: Apache-2.0


import iota_wallet as iw
import os
from dotenv import load_dotenv


# Load the env variables
load_dotenv()

# Get the stronghold password
#STRONGHOLD_PASSWORD = os.getenv('STRONGHOLD_PASSWORD')
STRONGHOLD_PASSWORD = 'password'


account_manager = iw.AccountManager(
    storage_path='./alice-database'
)  # note: `storage` and `storage_path` have to be declared together

account_manager.set_stronghold_password(STRONGHOLD_PASSWORD)

# mnemonic (seed) should be set only for new storage
# once the storage has been initialized earlier then you should omit this step
account_manager.store_mnemonic("Stronghold")

# ... continue from prev example 1a

# general Tangle specific options
client_options = {
    "nodes": [
        {
            "url": "https://api.lb-0.testnet.chrysalis2.com",
            "auth": None,
            "disabled": False
        }
    ],
    "local_pow": True
}

# an account is generated with the given alias via `account_initialiser`
account_initialiser = account_manager.create_account(client_options)
account_initialiser.alias('Alice')

# initialise account based via `account_initialiser`
# store it to db and sync with Tangle
account = account_initialiser.initialise()
print(f'Account created: {account.alias()}')