import csv
import threading
import time
import json
import urllib.request
from urllib.request import Request, urlopen
import datetime


import threading

class AsyncTask:
    def __init__(self):
        pass

    def TaskA(self):
        counter = 0
        Name = ['Timestamp', 'BTC', 'ETH', 'XRP', 'BCH']
        f1 = open('bithumb_balnce.csv', 'a', encoding='utf-8')
        f2 = open('coinone_balance.csv', 'a', encoding='utf-8')
#        f3 = open('korbit_balance.csv', 'a', encoding='utf-8')

        wr1 = csv.writer(f1)
        wr1.writerow(Name)
        wr2 = csv.writer(f2)
        wr2.writerow(Name)
#        wr3 = csv.writer(f3)


        while(counter < 3):                     #얼마나
            print('Process A')

            Time_thumb = int(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['date'])
            BTC_thumb = int(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['BTC']['closing_price'])
            ETH_thumb = int(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['ETH']['closing_price'])
            XRP_thumb = int(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['XRP']['closing_price'])
            BCH_thumb = int(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['BCH']['closing_price'])

            wr1.writerow([Time_thumb, BTC_thumb, ETH_thumb, XRP_thumb, BCH_thumb])

            Time_one = int(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['date'])
            BTC_one = int(json.loads(urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all').read())['btc']['last'])
            ETH_one = int(json.loads(urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all').read())['eth']['last'])
            XRP_one = int(json.loads(urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all').read())['xrp']['last'])
            BCH_one = int(json.loads(urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all').read())['bch']['last'])

            wr2.writerow([Time_one, BTC_one, ETH_one, XRP_one, BCH_one])

            '''
            Time_bit = int( json.loads(urllib.request.urlopen('https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw').read())['timestamp'])
            BTC_bit = int( json.loads(urllib.request.urlopen('https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw').read())['last'] )
            ETH_bit = int( json.loads(urllib.request.urlopen('https://api.korbit.co.kr/v1/ticker?currency_pair=eth_krw').read())['last'] )
            XRP_bit = int( json.loads(urllib.request.urlopen('https://api.korbit.co.kr/v1/ticker?currency_pair=xrp_krw').read())['last'] )
            BCH_bit = int( json.loads(urllib.request.urlopen('https://api.korbit.co.kr/v1/ticker?currency_pair=bch_krw').read())['last'] )
            wr3.writerow(Name)
            wr3.writerow([Time_bit, BTC_bit, ETH_bit, XRP_bit, BCH_bit])
            '''

            counter += 1

            print("Time: ", Time_thumb)
            print("BTC: ", BTC_thumb)
            print("ETH: ", ETH_thumb)
            print("XRP: ", XRP_thumb)
            print("BCH: ", BCH_thumb)

            print("Time: ", Time_one)
            print("BTC: ", BTC_one)
            print("ETH: ", ETH_one)
            print("XRP: ", XRP_one)
            print("BCH: ", BCH_one)
            '''
            print("Time: ", Time_bit)
            print("BTC: ", BTC_bit)
            print("ETH: ", ETH_bit)
            print("XRP: ", XRP_bit)
            print("BCH: ", BCH_bit)
            '''
            time.sleep(5)                       #몇초간격
        f1.close()
        f2.close()
#        f3.close()

def main():
    print('Async Function')

    at = AsyncTask()
    at.TaskA()


if __name__ == '__main__':
    main()
