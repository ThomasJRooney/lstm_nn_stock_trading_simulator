from conf.config import *

# paper trading
BASE_URL = 'https://paper-api.alpaca.markets'
# live trading
# BASE_URL = 'https://api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ACCOUNT_ACTIVITES_URL = '{}/v2/account/activities'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
POSITIONS_URL = '{}/v2/positions'.format(BASE_URL)
ASSETS_URL = '{}/v2/assets'.format(BASE_URL)
WATCHLISTS_URL = '{}/v2/watchlists'.format(BASE_URL)
CALENDAR_URL = '{}/v2/calendar'.format(BASE_URL)
CLOCK_URL = '{}/v2/clock'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
