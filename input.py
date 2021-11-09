"""
Holds all of the input functions
"""

#region input
def inputTickers():
    ticker_list = input("Input a list of tickers with spaces between each one: ").split()
    return ticker_list

def inputStandardTickers():
    add_to_list = input("Input the tickers with spaces between each one: ").split()
    return add_to_list

def inputCrypto():
    crypto_usd = []
    crypto_list = input("Type out the crypto tickers with spaces between each one: ").split()
 
    for i in crypto_list:
        i += "-USD"
        crypto_usd.append(i)
    
    return crypto_usd
#endregion