from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

infura_url = os.getenv("INFURIA_ENDPOINT")

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider(infura_url))
res = w3.isConnected()

if res is True:
    print("Connected.")
else:
    print("Not connected.")
 
# Get the latest block 
latest_block = w3.eth.get_block('latest')

# Method to verify adress:
is_address_valid = w3.isAddress('0x6dAc6E2Dace28369A6B884338B60f7CbBF7fb9be')

# Get the balance in an ethereum adress:
checksum = w3.toChecksumAddress('0xd7986a11f29fd623a800adb507c7702415ee7718')
balance = w3.eth.get_balance(checksum)

# Convert balance currency to something we know: ether
ether_value = w3.fromWei(balance, 'ether')
print(ether_value)