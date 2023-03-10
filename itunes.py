import requests
import json
import sys

if len(sys.argv)!=2:
    sys.exit("error")

try:
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    dict=response.json()
    dict_bpi=dict["bpi"]
    dict_USD=dict_bpi["USD"]
    coins=float((sys.argv[1]))
    rate_bitcoin_USD=float(dict_USD["rate_float"])
    amount=coins * rate_bitcoin_USD
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("error")
