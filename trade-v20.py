#!/usr/bin/env python
import v20
import requests
import ConfigParser

class Trade20():
    def __init__(self):
         Config = ConfigParser.ConfigParser()
         Config.read("./account.txt")
         self.id = Config.get("account", "id")
         self.token = Config.get("account", "token")
         self.instruments = Config.get("forex", "instrument")

    def showAccount(self):
        print self.id
        print self.token

    def listOrders(self):
        print "v20 is invalid for now."

mytrade = Trade20()
mytrade.showAccount()
