
import tdameritrade as td
import os

client_id = os.getenv('TDAMERITRADE_CLIENT_ID')
account_id = os.getenv('TDAMERITRADE_ACCOUNT_ID')
refresh_token = os.getenv('TDAMERITRADE_REFRESH_TOKEN')

# tdclient = td.TDClient(client_id=client_id, refresh_token=refresh_token, account_ids=[account_id])
c = td.TDClient()

symbol = 'AAPL'
periodType = 'day'
period = 1
frequencyType = 'minute'
# frequency = 1

print(c.history(symbol, periodType, period, frequencyType))
