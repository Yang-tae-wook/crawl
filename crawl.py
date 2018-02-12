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
        #f1 = open('bithumb_balnce.csv', 'a', encoding='utf-8')
        #f2 = open('coinone_balance.csv', 'a', encoding='utf-8')
        #f3 = open('korbit_balance.csv', 'a', encoding='utf-8')
        f4 = open('bitfinex_balance.csv', 'a', encoding='utf-8')

        #wr1 = csv.writer(f1)
    #    wr1.writerow(Name)
        #wr2 = csv.writer(f2)
        #wr2.writerow(Name)
        #wr3 = csv.writer(f3)
        #wr3.writerow(Name)
        wr4 = csv.writer(f4)
        wr4.writerow(Name)

        while(True):                     #얼마나
            print('Process A')

            #Time_thumb = round(float(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['date']))
            #BTC_thumb = int(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['BTC']['closing_price'])
            #ETH_thumb = float(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['ETH']['closing_price'])
            #XRP_thumb = int(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['XRP']['closing_price'])
            #BCH_thumb = int(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['BCH']['closing_price'])

            #wr1.writerow([Time_thumb, ETH_thumb])

            #Time_one = round(float(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['date']))
            #BTC_one = int(json.loads(urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all').read())['btc']['last'])
            #ETH_one = float(json.loads(urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all').read())['eth']['last'])
            #XRP_one = int(json.loads(urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all').read())['xrp']['last'])
            #BCH_one = int(json.loads(urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all').read())['bch']['last'])

            #wr2.writerow([Time_one, ETH_one])



            #Time_bit = round(float(json.loads(urllib.request.urlopen('https://api.bithumb.com/public/ticker/all').read())['data']['date']))
            '''
            reqBTC = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw' , headers={'User-Agent': 'Mozilla/5.0'})
            readBTC = urlopen(reqBTC).read()
            jsonBTC = json.loads(readBTC)
            FindBTC = jsonBTC['last']
            BTC_bit = int(FindBTC)

            reqETH = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=eth_krw' , headers={'User-Agent': 'Mozilla/5.0'})
            readETH = urlopen(reqETH).read()
            jsonETH = json.loads(readETH)
            FindETH = jsonETH['last']
            ETH_bit = float(FindETH)

            reqXRP = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=xrp_krw' , headers={'User-Agent': 'Mozilla/5.0'})
            readXRP = urlopen(reqXRP).read()
            jsonXRP = json.loads(readXRP)
            FindXRP = jsonXRP['last']
            XRP_bit = int(FindXRP)

            reqBCH = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=bch_krw' , headers={'User-Agent': 'Mozilla/5.0'})
            readBCH = urlopen(reqBCH).read()
            jsonBCH = json.loads(readBCH)
            FindBCH = jsonBCH['last']
            BCH_bit = int(FindBCH)
            '''

            #wr3.writerow([Time_bit, ETH_bit])



            Time_finex = round(float(json.loads(urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/btcusd').read())['timestamp']))*1000
            BTC_finex = float(json.loads(urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/btcusd').read())['last_price'])
            #ETH_finex = float(json.loads(urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/ethusd').read())['last_price'])
            #XRP_finex = float(json.loads(urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/xrpusd').read())['last_price'])
            #BCH_finex = float(json.loads(urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/bchusd').read())['last_price'])

            #wr4.writerow([Time_finex, ETH_finex])
            counter += 1

            #print("Time: ", Time_thumb)
            #print("BTC: ", BTC_thumb)
            #print("ETH: ", ETH_thumb)
            #print("XRP: ", XRP_thumb)
            #print("BCH: ", BCH_thumb)

            #print("Time: ", Time_one)
            #print("BTC: ", BTC_one)
            #print("ETH: ", ETH_one)
            #print("XRP: ", XRP_one)
            #print("BCH: ", BCH_one)

            #print("Time: ", Time_bit)
            #print("BTC: ", BTC_bit)
            #print("ETH: ", ETH_bit)
            #print("XRP: ", XRP_bit)
            #print("BCH: ", BCH_bit)


            print("Time: ", Time_finex)
            #print("BTC: ", BTC_finex)
            #print("ETH: ", ETH_finex)
            #print("XRP: ", XRP_finex)
            #print("BCH: ", BCH_finex)

            time.sleep(10)                       #몇초간격
        #f1.close()
        #f2.close()
        #f3.close()
        f4.close()


def main():
    print('Async Function')

    at = AsyncTask()
    at.TaskA()


if __name__ == '__main__':
    main()
