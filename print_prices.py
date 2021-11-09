"""
Holds functions to print the prices for the tickers
"""
#region print
def printLivePrices(live_price_list):
    print("\n")
    print("Standard Stock Tickers:")
    for i in live_price_list:
        print(i)

def printCryptoPrices(crypto_price_list):
    print("Crypto Tickers:")
    for i in crypto_price_list:
        print(i)
#endregion