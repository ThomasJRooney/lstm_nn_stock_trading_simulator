import requests, json
from globals import *

#Trader class provides basic trading functions to a trader object
#This is the parent class of all other strategies built on it

class StockTrader():

    def get_account(self):
        r = requests.get(ACCOUNT_URL, headers = HEADERS)
        return json.loads(r.content)

    # may need parameters
    def get_account_activities(self):
        r = requests.get(ACCOUNT_ACTIVITES_URL, headers = HEADERS)
        return json.loads(r.content)

    def create_order(self, symbol, qty, side, type, time_in_force):
        data = {
            "symbol" : symbol,
            "qty" : qty,
            "side" : side,
            "type" : type,
            "time_in_force" : time_in_force
        }
        r = requests.post(ORDERS_URL, json = data, headers = HEADERS)
        return json.loads(r.content)

    def get_orders(self):
        r = requests.get(ORDERS_URL, headers = HEADERS)
        return json.loads(r.content)

    def get_positions(self):
        r = requests.get(POSITIONS_URL, headers = HEADERS)
        return json.loads(r.content)

    def close_all_positions(self):
        r = requests.delete(POSITIONS_URL, headers = HEADERS)
        return json.loads(r.content)

    def close_position(self, symbol):
        r = requests.delete(POSITIONS_URL + '/' + symbol, headers = HEADERS)
        return json.loads(r.content)

    def get_assets(self):
        r = requests.get(ASSETS_URL, headers = HEADERS)
        return json.loads(r.content)

    def get_asset(self, symbol):
        r = requests.get(ASSETS_URL + '/' + symbol, headers = HEADERS)
        return json.loads(r.content)

    def get_watchlists(self):
        r = requests.get(WATCHLISTS_URL, headers = HEADERS)
        return json.loads(r.content)

    def create_watchlist(self, name, symbols):
        data = {
            "name" : name,
            "symbols" : symbols
        }
        r = requests.post(WATCHLISTS_URL, json = data, headers = HEADERS)
        return json.loads(r.content)

    def get_calendar(self, start, end):
        data = {
            "start" : start,
            "end" : end
        }
        r = requests.get(CALENDAR_URL, json = data, headers = HEADERS)
        return json.loads(r.content)

    def get_clock(self):
        r = requests.get(CLOCK_URL, headers = HEADERS)
        return json.loads(r.content)
