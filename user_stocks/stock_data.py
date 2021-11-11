#region imports and global variables
from yahoo_fin import stock_info as si
import cbpro
from slowprint.slowprint import slowprint
# Public Client for CoinBase Pro
pc = cbpro.PublicClient()
#endregion
class StockData():
    class Input():
        #region input
        def inputTickers(self):
            slowprint("Input a list of tickers with spaces between each one: ", 0.3)
            ticker_list = input().split()
            return ticker_list

        def inputStandardTickers(self):
            slowprint("Input the tickers with spaces between each one: ", 0.3)
            add_to_list = input().split()
            return add_to_list

        def inputCrypto(self):
            crypto_usd = []
            slowprint("Type out the crypto tickers with spaces between each one: ", 0.3)
            crypto_list = input().split()
        
            for i in crypto_list:
                i += "-USD"
                crypto_usd.append(i)
            
            return crypto_usd
        #endregion

    class Market():
        """
        Holds the functions to get the prices for the tickers, and the market status
        """
        #region market status
        def getMarketStatus(self):
            """
            Gets the market status through yahoo_fin's get_market_status() function.\n
            """
            market_status = si.get_market_status()
            return market_status

        def printMarketStatus(self):
            """
            Takes getMarketStatus() value and prints out the status of the market.
            """
            market_status = StockData.Market.getMarketStatus(StockData)
            if market_status == "POST":
                slowprint("We are in the Post-Market period.\n", 0.3)
            elif market_status == "PRE":
                slowprint("We are in the Pre-Market period.\n", 0.3)
            elif market_status == "POSTPOST":
                slowprint("The Market is closed for today.\n", 0.3)
            else:
                slowprint("The market is Open.\n", 0.3)
        #endregion

        #region get prices
        def getCryptoPrice(self, crypto_list):
            """
            Takes the input crypto_list loops through it, and returns the prices in a list.
            """
            crypto_price = ""
            crypto_price_list = []

            for items in crypto_list:
                crypto = pc.get_product_ticker(product_id= items)
                if 'message' in crypto:
                    pass
                else:
                    crypto_price = "\n" + items + ":\n" + "$" + crypto['price'] + "\n"
                    crypto_price_list.append(crypto_price)
            
            return crypto_price_list

        def getLivePrice(self, ticker_list):
            """
            Takes the input ticker_list and loops through each one\n
            returning either the Pre, Live, or Post market value depending on what getMarketStatus() returns
            """
            market_status = StockData.Market.getMarketStatus(StockData)
            premarket_price = ""
            live_price = ""
            postmarket_price = ""
            price_list = []

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

    class Print():
        """
        Holds all of the input functions
        """
        #region print
        def printLivePrices(self, live_price_list):
            stock_price = ""

            for i in live_price_list:
                stock_price += i    
            return stock_price    

        def printCryptoPrices(self, crypto_price_list):
            crypto_price = ""
            for i in crypto_price_list:
                crypto_price += i
            return crypto_price
        #endregion