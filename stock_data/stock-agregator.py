#region imports
from input import inputTickers, inputCrypto, inputStandardTickers
from get_prices import getMarketStatus, getLivePrice, getCryptoPrice, printMarketStatus
from print_prices import printLivePrices, printCryptoPrices
from time import time, sleep
import keyboard
#endregion

def cryptoOrStandard(tickers):
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

    while t_f:
        y_n = input("Do you want to add more tickers? ")

        if y_n == "Y" or y_n == "y":
            c_s = input("Do you want to input a Cryptocurrency (C) ticker or a Standard(S) ticker? ")
            if c_s == "C" or c_s == "c":
                crypto_list = inputCrypto()
                for i in crypto_list:
                    empty_crypto.append(i)
                full_crypto_list = getCryptoPrice(empty_crypto)
            
            elif c_s == "S" or c_s == "s":
                standard_list = inputStandardTickers()
                for i in standard_list:
                    tickers.append(i)
                full_list = getLivePrice(tickers)
            
            else:
                print("Please put c or s.")
            
        elif y_n == "N" or y_n == "n":
            t_f = False
            ticker_list = getLivePrice(tickers)

            if full_list and full_crypto_list:
                print(printLivePrices(full_list))
                print(printCryptoPrices(full_crypto_list))
            elif full_list:
                print(printLivePrices(full_list))
            elif full_crypto_list:
                print(printLivePrices(ticker_list))
                print(printCryptoPrices(full_crypto_list))
            else:
                print(printLivePrices(ticker_list))
        else:
            print("Please put y or n.")


def priceAllDay(tickers):
    t_f = True
    # i = 0
    while t_f:
        prices = getLivePrice(tickers)
        print(printLivePrices(prices))
        sleep(60 - time() % 60)

       # this = input("Stop(s) or Continue (anything else)?")
       # if this == "c":
           # while i < 1:
               # prices = getLivePrice(tickers)
               # sleep(60 - time() % 60)
               # i += 1
        # elif this == "s":
           # print("Price checking ended")
            # break


def main():
    printMarketStatus()
    tickers = inputTickers()
    priceAllDay(tickers)

if __name__ == "__main__":
    main() 