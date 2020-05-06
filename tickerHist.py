
import tdameritrade as td
import os
import csv
from datetime import datetime as dt
from pprint import pprint


client_id = os.getenv('TDAMERITRADE_CLIENT_ID')
account_id = os.getenv('TDAMERITRADE_ACCOUNT_ID')
refresh_token = os.getenv('TDAMERITRADE_REFRESH_TOKEN')

# tdclient = td.TDClient(client_id=client_id, refresh_token=refresh_token, account_ids=[account_id])
c = td.TDClient()
# symbol = 'GLD'


def create_ticker_candles_dict(symbol):

    periodType = 'day'
    period = 1
    frequencyType = 'minute'
    tkrhist = c.history(symbol, periodType, period, frequencyType)
    ticker_candles = dict(datetime=[], open=[], close=[])

    for candle in tkrhist['candles']:
        date = candle['datetime']/1e3
        ticker_candles['datetime'].append(
            dt.fromtimestamp(date))
        ticker_candles['open'].append(candle['open'])
        ticker_candles['close'].append(candle['close'])

    return ticker_candles

    # print(ticker_candles['datetime'][0])

# with open('gldticker.csv', 'w', newline='') as f:
#     fieldnames = ['datetime', 'open', 'close']
#     writerobj = csv.DictWriter(f, fieldnames=fieldnames)

#     writerobj.writeheader()
#     for candle in candles:

#         writerobj.writerow(
#             {'datetime': candle['datetime'], 'open': candle['open'], 'close': candle['close']})
