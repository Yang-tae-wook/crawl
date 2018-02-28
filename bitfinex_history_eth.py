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


            url1 = "https://api.bitfinex.com/v2/candles/trade:5m:tETHUSD/hist"
            url2 = "https://api.bitfinex.com/v2/candles/trade:5m:tQTMUSD/hist"


            params = { 'start': end-35700000, 'end': end }
            r1 = requests.get(url1, params = params)
            r2 = requests.get(url2, params = params)
            data1 = r1.json()
            data2 = r2.json()
            print(data1)
            print(data2)
            end = end - 35700000

            data_arr1 = np.array(data1)
            data_arr2 = np.array(data2)


            close_data1 = data_arr1[:,0:3:2]
            print(close_data1)
            close_data2 = data_arr2[:,0:3:2]
            print(close_data2)

            for row in close_data1:
                wr1.writerow(row)
            for row in close_data2:
                wr2.writerow(row)




            time.sleep(10)
        f.close()


def main():
    print('Async Function')

    at = AsyncTask()
    at.TaskA()


if __name__ == '__main__':
    main()
