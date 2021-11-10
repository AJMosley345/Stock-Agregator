"""
Holds functions to print the prices for the tickers
"""
#region print
def printLivePrices(live_price_list):
    stock_price = ""
    # print("\n")
    # print("Standard Stock Tickers:")
    for i in live_price_list:
        stock_price += i    
    return stock_price    

def printCryptoPrices(crypto_price_list):
    crypto_price = ""
    # print("Crypto Tickers:")
    for i in crypto_price_list:
        crypto_price += i
    return crypto_price
#endregion