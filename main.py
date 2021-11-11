# main.py
#region imports, objects and global variable
from slowprint.slowprint import slowprint
import user_stocks.user_stocks as us
import ticker_scraper.top_tickers as tp
#endregion

def main():
    welcome = [
        "------------------------------------------------------------",
        "Welcome to the Stock Agregator.\n",
        "There are 2 options: \n", 
        "Either 1: get the prices of the most active stocks and cryptocurrencies.\n",
        "Or\n",
        "2: Input your own stocks/crypto and get the current price.\n",
        "Either one can be saved to a spreadsheet (csv) or text file to be used later.\n",
        "1 or 2?",
    ]
    for i in welcome:
        slowprint(i, .3)
    one_two = input()

    if one_two == "1":
        tp.getTopStocks()
    elif one_two == "2":
        us.inputStocks()
    else:
        print("Please enter 1 or 2. ")

    


if __name__ == "__main__":
    main()