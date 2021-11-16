# main.py
#region imports, objects and global variable
from slowprint.slowprint import slowprint
from ticker_scraper.top_tickers import getTopStocks
from user_stocks.user_stocks import inputStocks
from user_stocks.stock_data import getLivePrice, printLivePrices, printMarketStatus
import sys
sys.path.append("/home/aj/Projects/Python-Projects/Python-Bot")
from get_wsb_stocks import popTickersList
from get_crypto import runCrypto
from get_stocks import popTickersListStock
#endregion

def main():
    j = 0
    welcome = [
        "|--------------------------------------------------------------------|",
        "| Welcome to the Stock Agregator                                     |",
        "| There are currently 3 options                                      |", 
        "| 1.Get the prices of the most active stocks and cryptocurrencies.   |",
        "| 2.Input your own stocks/crypto and get the current price.          |",
        "| 3.Get the prices of the most popular stocks on r/WSB or r/Stocks   |",
        "|   and the most popular cryptocurrencies from r/Cryptocurrency      |",
        "| Select 1, 2 or 3                                                   |",
        "|--------------------------------------------------------------------|",
    ]
    for i in welcome:
        if j == 2:
            printMarketStatus()
        slowprint(i, .2)
        j += 1
    one_two = input("\n")

    if one_two == "1":
        getTopStocks()
    elif one_two == "2":
        inputStocks()
    elif one_two == "3":
        slowprint("Do you want the most popular stocks from r/WallStreetBets (w) or r/Stocks (s)?", .2)
        w_s = input()
        if w_s == "w" or w_s == "W":
            slowprint("Prices of the most popular stocks in r/WallStreetBets\n", .2)
            pop_list = popTickersList()
            price_list = getLivePrice(pop_list)
            slowprint(printLivePrices(price_list), .2)
            runCrypto()
        elif w_s == "s" or w_s == "S":
            slowprint("Prices of the most popular stocks in r/Stocks\n", .2)
            pop_list = popTickersListStock()
            price_list = getLivePrice(pop_list)
            slowprint(printLivePrices(price_list), .2)
            runCrypto()
        else:
            slowprint("Please put w or s.", .2)
    else:
        print("Please enter 1, 2 or 3. ")


if __name__ == "__main__":
    main()