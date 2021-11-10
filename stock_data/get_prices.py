"""
Holds the functions to get the prices for the tickers, and the market status
"""
#region imports
from yahoo_fin import stock_info as si
import cbpro

# Public Client for CoinBase Pro
pc = cbpro.PublicClient()

def getMarketStatus():
    """
    Gets the market status through yahoo_fin's get_market_status() function.\n
    """
    market_status = si.get_market_status()
    return market_status

def printMarketStatus():
    """
    Takes getMarketStatus() value and prints out the status of the market.
    """
    market_status = getMarketStatus()
    if market_status == "POST":
        print("We are in the Post-Market period.\n")
    elif market_status == "PRE":
        print("We are in the Pre-Market period.\n")
    elif market_status == "POSTPOST":
        print("The Market is closed for today.\n")
    else:
        print("The market is Open.\n")


#region get prices
def getCryptoPrice(crypto_list):
    """
    Takes the input crypto_list loops through it, and returns the prices in a list.
    """
    crypto_price = ""
    crypto_price_list = ['']

    for items in crypto_list:
        crypto = pc.get_product_ticker(product_id=items)
        crypto_price = items + ":\n" + "$" + crypto['price'] + "\n"
        crypto_price_list.append(crypto_price)
    
    return crypto_price_list

def getLivePrice(ticker_list):
    """
    Takes the input ticker_list and loops through each one\n
    returning either the Pre, Live, or Post market value depending on what getMarketStatus() returns
    """

    market_status = getMarketStatus()
    premarket_price = ""
    live_price = ""
    postmarket_price = ""
    price_list = ['']

    if market_status == "PRE":
        for items in ticker_list:
            stock = si.get_premarket_price(items)
            premarket_price = "\n" + items + ":\n" + "$" + ("%.2f" % stock) + "\n"
            price_list.append(premarket_price)
    elif market_status == "POST" or market_status == "POSTPOST":
        for items in ticker_list:
            stock = si.get_postmarket_price(items)
            postmarket_price = "\n" + items + ":\n" + "$" + ("%.2f" % stock) + "\n"
            price_list.append(postmarket_price)
    else:
        for items in ticker_list:
            stock = si.get_live_price(items)
            live_price = "\n" + items + ":\n" + "$" + ("%.2f" % stock) + "\n"
            price_list.append(live_price)
    
    return price_list

#endregion