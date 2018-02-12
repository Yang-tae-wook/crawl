import requests
import csv
import threading
import time
import json
import datetime

class AsyncTask:
    def __init__(self):
        pass

    def TaskA(self):
        counter = 1
        Name = ['Timestamp', 'OPEN', 'CLOSE', 'HIGH', 'LOW', 'VOLUMN']
        f = open('bitfinex_hist_eth.csv', 'w', encoding='utf-8')

        wr = csv.writer(f)
        wr.writerow(Name)

        end = 1518412899000

        while(end > 1458149797000):
            url = 'https://api.bitfinex.com/v2/candles/trade:5m:tETHUSD/hist'
            params = { 'start': end-35700000, 'end': end }
            r = requests.get(url, params = params)
            data = r.json()
            print(counter)
            end = end - 35700000
            for row in data:
                #print(row)
                wr.writerow(row)
            counter += 1
            time.sleep(5)
        f.close()


def main():
    print('Async Function')

    at = AsyncTask()
    at.TaskA()


if __name__ == '__main__':
    main()
