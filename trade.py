#!/usr/bin/env python
#
# This is a script testing all APIs of oandapy
#

import oandapy
import ConfigParser
from pprint import pprint
from datetime import datetime, timedelta

Config = ConfigParser.ConfigParser()
Config.read("./account.txt")

ACCOUNT = Config.get("account", "id")
TOKEN = Config.get("account", "token")
INSTRUMENT = Config.get("forex", "instrument")

api = oandapy.API(access_token=TOKEN)

#
# Get API information
#
print "API URL:\t%s" % api.api_url

#
# Get instruments
#
print "***********************\n"
print "Available instruments:"
print "***********************\n"
pprint(api.get_instruments(account_id=ACCOUNT))

#
# Get Accounts information
#
info = api.get_accounts()
for i in info["accounts"]:
    print "***********************\n"
    print "Account information:\n"
    print "***********************\n"
    pprint(api.get_account(i["accountId"]))

#
# Get instruments position
#
print "***********************\n"
print "Position:\n"
print "***********************\n"
pprint(api.get_positions(account_id=ACCOUNT))

#
# Get price of exact ACCOUNT, INSTRUMENT
#
print "***********************\n"
print "Prices of %s:\n" % INSTRUMENT
print "***********************\n"
price_response = api.get_prices(instruments=INSTRUMENT)
pprint(price_response)

#
# Get orders
#
print "***********************\n"
print "Orders information:\n"
print "***********************\n"
orders = api.get_orders(account_id=ACCOUNT)
pprint(orders)

#
# Open buy order
#
print "***********************\n"
print "Open buy order:\n"
print "***********************\n"
trade_expire = datetime.utcnow() + timedelta(days=1)
trade_expire = trade_expire.isoformat("T") + "Z"

# Units must be greater than 1
buy_response = api.create_order(ACCOUNT,
    instrument=INSTRUMENT,
    units=1,
    side='buy',
    type='limit',
    price=1.15,
    expiry=trade_expire
)
pprint(buy_response)

#
# Close buy orders
#
print "***********************\n"
print "Close Buy order:\n"
print "***********************\n"
#close_response = api.close_order(account_id=ACCOUNT, buy_response["orderOpened"]["id"])

#
# Get transactions 
#
print "***********************\n"
print "Transactions:\n"
print "***********************\n"
pprint(api.get_transaction_history(account_id=ACCOUNT))
