import requests
import csv
import threading
import time
import json
import datetime
import numpy as np

class AsyncTask:
    def __init__(self):
        pass

    def TaskA(self):

        Name = ['Timestamp', 'CLOSE']
        f1 = open('bitfinex_hist_eth.csv', 'w', encoding='utf-8')
        f2 = open('bitfinex_hist_qtum.csv', 'w', encoding='utf-8')

        wr1 = csv.writer(f1)
        wr2 = csv.writer(f2)
        wr1.writerow(Name)
        wr2.writerow(Name)

        end = 1519788177000

        while(end > 1506816000000):
            coin_type=["ETH", "QTM"]

            for i in coin_type:
                url = "https://api.bitfinex.com/v2/candles/trade:5m:t"+i+"USD/hist"


                params = { 'start': end-35700000, 'end': end }
                r = requests.get(url, params = params)
                data = r.json()
                print(data)
                end = end - 35700000

                data_arr = np.array(data)

                close_data = data_arr[:,0:3:2]
                print(close_data)

                for row in close_data:
                    print(row)
                    if i == "ETH":
                        wr1.writerow(row)
                    else:
                        wr2.writerow(row)




            time.sleep(10)

        f.close()


def main():
    print('Async Function')

    at = AsyncTask()
    at.TaskA()


if __name__ == '__main__':
    main()
