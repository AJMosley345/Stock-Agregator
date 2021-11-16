# main.py
#region imports, objects and global variable
from slowprint.slowprint import slowprint
from ticker_scraper.top_tickers import getTopStocks
from user_stocks.user_stocks import inputStocks
from user_stocks.stock_data import getLivePrice, printLivePrices, printMarketStatus
import sys
sys.path.append("/home/aj/Projects/Python-Projects/Python-Bot")
from get_wsb_stocks import popTickersList
#endregion

def main():
    welcome = [
        "-------------------------------------------------------------------",
        "                  Welcome to the Stock Agregator                   \n",
        "                       There are 3 options                           \n", 
        "1: Get the prices of the most active stocks and cryptocurrencies.\n",
        "2: Input your own stocks/crypto and get the current price.\n",
        "3: Get the prices of the most popular stocks on r/WallStreetBets\n",
        "1, 2 or 3?",
    ]

    for i in welcome:
        slowprint(i, .2)
    one_two = input("\n")

    if one_two == "1":
        getTopStocks()
    elif one_two == "2":
        inputStocks()
    elif one_two == "3":
        printMarketStatus()
        slowprint("Prices of the most popular stocks in r/WallStreetBets\n", .3)
        pop_list = popTickersList()
        price_list = getLivePrice(pop_list)
        slowprint(printLivePrices(price_list), .3)
    else:
        print("Please enter 1, 2 or 3. ")

    


if __name__ == "__main__":
    main()