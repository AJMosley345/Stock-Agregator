#region imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import yahoo_fin.stock_info as yf
#endregion

#region get symbols
def getNTickers():
    s_list = ""
    tickers = yf.tickers_nasdaq()
    for i in tickers:
        s_list += i + "\n"
    return s_list

def getCSymbols():
    c_url = 'https://coinmarketcap.com/all/views/all/'
    c_symbols = ""
    c_url_request = requests.get(c_url)

    c_page = BeautifulSoup(c_url_request.content, "html.parser")
    
    c_tickers = c_page.find_all(
            'td', 
            class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--hide-sm cmc-table__cell--sort-by__symbol",
            limit=11
    )

    for symbl in c_tickers:
        symbol_name = symbl.find('div', class_="")
        c_symbols += symbol_name.text + "\n"

    return c_symbols
#endregion

def openAndWrite(s_list, c_symbols):
    with open("standard_ticker_list.txt", 'w') as f:
        f.truncate()
        f.write(s_list)

    with open("crypto_list.txt", 'w') as f:
        f.truncate()
        f.write(c_symbols)

def main():
    s_list = getNTickers()
    c_symbols = getCSymbols()
    openAndWrite(s_list, c_symbols)

if __name__ == "__main__":
    main()
