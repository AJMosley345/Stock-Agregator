#region import
import user_stocks.stock_data as sd 
from ticker_scraper import (
    get_ticker_list as tl,
    write_to_csv as cs
)
from slowprint.slowprint import *
#endregion

#region creating objects
sto = sd.StockData()
ts = tl.Tickers()
#endregion

#region print pretty
def printTopCrypto():
    print("Top Cryptocurrencies:")
    crypto_list = ts.getCSymbols()
    crypto = sto.Market.getCryptoPrice(sto, crypto_list)
    slowprint(sto.Print.printCryptoPrices(sto, crypto), .3)
    return crypto

def printActiveStocks():
    print("Most Active Stocks Today:")
    ticker_list = ts.getNTickers()
    price = sto.Market.getLivePrice(sto, ticker_list)
    slowprint(sto.Print.printLivePrices(sto, price), .3)

    return price
#endregion

def getTopStocks():
    sto.Market.printMarketStatus(sto)
    crypto = printTopCrypto()
    ticker_list = printActiveStocks()
    cs.writeToFile(ticker_list, crypto)
