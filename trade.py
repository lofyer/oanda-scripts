#!/usr/bin/env python
#
# This is a script testing all APIs of oandapy
#

import oandapy
import ConfigParser
from pprint import pprint
from datetime import datetime, timedelta

class Trade():
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("./account.txt")
        self.id = Config.get("account", "id")
        self.token = Config.get("account", "token")
        self.instruments = Config.get("forex", "instrument")
        self.api = oandapy.API(access_token=self.token)

    def showAccount(self):
        print "id: " + self.id
        print "token: " + self.token
        print "url: " + self.api.api_url

    def get_accounts(self):
        all_accounts = self.api.get_accounts()
        for i in all_accounts["accounts"]:
            pprint(self.api.get_account(i["accountId"]))
    
    def get_instruments(self):
        print "Available instruments:"
        pprint(self.api.get_instruments(account_id=self.id))

    def get_orders(self):
        pprint(self.api.get_orders(account_id=self.id))

    def get_positions(self):
        pprint(self.api.get_positions(account_id=self.id))

    def get_prices(self):
        pprint(self.api.get_prices(instruments=self.instruments))

    def get_orders(self):
        pprint(self.api.get_orders(account_id=self.id))

    def open_order(self):
        trade_expire = datetime.utcnow() + timedelta(days=1)
        trade_expire = trade_expire.isoformat("T") + "Z"
        self.buy_response = self.api.create_order(self.id,
                instrument=self.instruments,
                unit=1,
                side='buy',
                type='limit',
                price=1.15,
                expiry=trade_expire
                )
        pprint(buy_response)

    def close_order(self):
        pprint(self.api.close_order(account_id=self.id, self.buy_response["orderOpened"]["id"]))

    def get_transactions(self):
        pprint(self.api.get_transaction_history(account_id=self.id)
    

trade = Trade()
#trade.showAccount()
#trade.get_accounts()
#trade.get_instruments()
#trade.get_orders()
#trade.get_positions()
#trade.get_prices()
#trade.get_orders()
#trade.open_order()
#trade.close_order()
#trade.get_transactions()
