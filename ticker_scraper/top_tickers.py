#region import
from user_stocks.stock_data import ( 
    printLivePrices, 
    printCryptoPrices, 
    getCryptoPrice, 
    getLivePrice, 
    printMarketStatus,
) 
from ticker_scraper.get_ticker_list import (
   getNTickers,
   getCSymbols
)
from slowprint.slowprint import *
#endregion

#region print pretty
def printTopCrypto():
    print("Top Cryptocurrencies:")
    crypto_list = getCSymbols()
    crypto = getCryptoPrice(crypto_list)
    slowprint(printCryptoPrices(crypto), .3)
    return crypto

def printActiveStocks():
    print("Most Active Stocks Today:")
    ticker_list = getNTickers()
    price = getLivePrice(ticker_list)
    slowprint(printLivePrices(price), .3)

    return price
#endregion

def getTopStocks():
    printMarketStatus()
    ticker_list = printActiveStocks()
    crypto = printTopCrypto()
    # cs.writeToFile(ticker_list, crypto)
