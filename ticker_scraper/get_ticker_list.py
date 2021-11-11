#region imports
from bs4 import BeautifulSoup
import requests
#endregion
class Tickers():
    #region get symbols
    def getNTickers(self):
        #region variables
        # Initializing empty variables
        s_tickers = ""
        s_list = []
        # Gets URL content
        s_url = 'https://money.cnn.com/data/hotstocks/'
        s_url_request = requests.get(s_url)
        s_page = BeautifulSoup(s_url_request.content, "html.parser")
        #endregion

        #region main
        table_container = s_page.find(
                'table',
                class_="wsod_dataTable wsod_dataTableBigAlt"
        )
        for tickers in table_container.find_all('a', class_='wsod_symbol'):
            symbol_name = tickers.contents[0]
            s_tickers = symbol_name
            s_list.append(s_tickers)
        #endregion
        
        return s_list

    def getCSymbols(self):
        #region variables
        c_url = 'https://coinmarketcap.com/all/views/all/'
        c_symbols = ""
        c_symbol_list = []
        c_url_request = requests.get(c_url)
        c_page = BeautifulSoup(c_url_request.content, "html.parser")
        #endregion

        #region main
        c_tickers = c_page.find_all(
                'td', 
                class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--hide-sm cmc-table__cell--sort-by__symbol",
                limit=11
        )

        for symbl in c_tickers:
            symbol_name = symbl.find('div', class_="")
            c_symbols = symbol_name.text + '-USD'
            c_symbol_list.append(c_symbols)
        #endregion

        return c_symbol_list
    #endregion

