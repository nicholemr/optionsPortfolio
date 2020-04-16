import csv
from pprint import pprint


def load_trade_history():
    log_dic = {}
    with open('tastyworks_files/tastyworks_transactions_x3019_2020-04-07_2020-04-14.csv', newline='') as csvfile:
        fndds = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in fndds:
            if count == 0:
                print(row)
            else:
                row_str = ', '.join(row)
                row_str_fields = row_str.split(',')
                # food_records[]={'GWP':}
                # print(row_str_fields)
                date = row_str_fields[0]
                open_or_close = row_str_fields[2].split('_')[2]
                ticker = row_str_fields[-4]
                value = float(row_str_fields[6])
                qty = round(float(row_str_fields[7]))
                exp = row_str_fields[-3]
                strike_price = float(row_str_fields[-2])
                call_or_put = row_str_fields[-1]
                if date not in log_dic:
                    log_dic[date] = {'open_or_close': open_or_close, 'ticker': ticker, 'credit_debit': value,
                                     'qty': qty, 'exp': exp, 'strike_prices': [strike_price], 'call_or_put': call_or_put}
                else:
                    log_dic[date]['credit_debit'] += value
                    log_dic[date]['strike_prices'].append(strike_price)

            count += 1
            # check if open:
    pprint(log_dic)


load_trade_history()
