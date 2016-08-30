#!/usr/bin/env python
import oandapy
import ConfigParser
from pprint import pprint
from datetime import datetime, timedelta

Config = ConfigParser.ConfigParser()
Config.read("./account.txt")

ACCOUNT = Config.get("account", "id")
TOKEN = Config.get("account", "token")

api = oandapy.API(access_token=TOKEN)

#
# Get Account information
#
info = api.get_accounts()
for i in info["accounts"]:
    print "Account information:\n"
    pprint(api.get_account(i["accountId"]))

#
# Get price
#
price_response = api.get_prices(account_id=ACCOUNT, instruments='EUR_USD, EUR_GBP, EUR_JPY,')

#
# Get orders
#
print "Orders information:\n"
orders = api.get_orders(account_id=ACCOUNT)
pprint(orders)

#
# Open test order
#
print "Buy order:\n"
trade_expire = datetime.utcnow() + timedelta(days=1)
trade_expire = trade_expire.isoformat("T") + "Z"

buy_response = api.create_order(ACCOUNT,
    instrument="USD_CAD",
    units=10,
    side='buy',
    type='limit',
    price=1.15,
    expiry=trade_expire
)
pprint(buy_response)

#
# Close buy orders
#
print "Close Buy order:\n"
#close_response = api.close_order(account_id=ACCOUNT, buy_response["orderOpened"]["id"])
