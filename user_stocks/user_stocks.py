# stock_agregator.py

#region imports and global variables
import user_stocks.stock_data as sd
import sys
from slowprint.slowprint import slowprint
sys.path.append("/home/aj/Projects/Python-Projects/Stock-Agregator/ticker_scraper")
import write_to_csv as cs

gp = sd.StockData.Market()
pr = sd.StockData.Print()
inp = sd.StockData.Input()
#endregion

def cryptoOrStandard(tickers):
    #region head
    """
    Main part of the program that asks if the user wants to input more tickers\n
    If no then it returns the initial ticker list\n
    If yes, then it asks if the user wants to add a Cryptocurrency ticker or a Standard ticker\n
    Then it repeats and adds until the user inputs N
    """
    t_f = True
    empty_crypto = []
    full_crypto_list = []
    full_list = []
    #endregion
    while t_f:
        #region main loop
        slowprint("Do you want to add more tickers? (y/n) ", 0.3)
        y_n = input()
        if y_n == "Y" or y_n == "y":
            #region crypto or standard
            slowprint("Do you want to input a Cryptocurrency (C) ticker or a Standard(S) ticker? ", 0.3)
            c_s = input()
            if c_s == "C" or c_s == "c":
                crypto_list = inp.inputCrypto()
                for i in crypto_list:
                    empty_crypto.append(i)
                full_crypto_list = gp.getCryptoPrice(empty_crypto)
            elif c_s == "S" or c_s == "s":
                standard_list = inp.inputStandardTickers()
                for i in standard_list:
                    tickers.append(i)
                full_list = gp.getLivePrice(tickers)
            else:
                slowprint("Please put c or s.", 0.2)
            #endregion 
        elif y_n == "N" or y_n == "n":
            t_f = False
            #region print lists
            ticker_list = gp.getLivePrice(tickers)

            if full_list and full_crypto_list:
                slowprint(pr.printLivePrices(full_list), 0.3)
                slowprint(pr.printCryptoPrices(full_crypto_list), 0.3)
            elif full_list:
                slowprint(pr.printLivePrices(full_list), 0.3)
            elif full_crypto_list:
                slowprint(pr.printLivePrices(ticker_list), 0.3)
                slowprint(pr.printCryptoPrices(full_crypto_list), 0.3)
            else:
                full_list = ticker_list
                slowprint(pr.printLivePrices(full_list), 0.3)
            #endregion
        else:
            slowprint("Please put y or n.", 0.2)
        #endregion
    return full_list, full_crypto_list

def inputStocks():
    gp.printMarketStatus()
    tickers = inp.inputTickers()
    full_ticker_list, crypto_list = cryptoOrStandard(tickers)

    cs.writeAndOpen(full_ticker_list, crypto_list)
