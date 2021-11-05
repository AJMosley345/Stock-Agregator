#region imports
# Raw Data
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

# Source
import yfinance as yf

# Visualization
import plotly.graph_objects as go
import plotly.express as px

# Google Drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#endregion

# Variables
gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 
ticker_list=['GME', 'UBER', 'MSFT']

def get_data(stock_list):
#region function
    """
    Downloads the stock data of list, converts it into a format that's more easily read\n
    Then puts the dataframe along the specficed axis\n
    Finally makes it so the dataframe only shows 'Open', 'High', 'Low', and 'Ticker', and returns it
    """
    ticker_list = stock_list
    df_list = list()

    for ticker in ticker_list:
        ticker_data = yf.download(
                ticker,
                period='1d',
                interval='5m',
                group_by='ticker',
                rounding=True
        )
        ticker_data['Ticker'] = ticker
        df_list.append(ticker_data)

    df = pd.concat(df_list)
    print(df)
    df = df[['Open', 'High', 'Low', 'Ticker']]
    return df
#endregion

def make_csv(dataframe):
#region function
    """
    Creates and empty csv file.\n 
    Opens it, erases the previous contents and writes the new dataframe to it
    """
    
    df = dataframe
    data=pd.DataFrame()
    data.to_csv('stock_data.csv')
    sprd = open('stock_data.csv', 'r+')
    sprd.truncate(0)
    df.to_csv(sprd)

#endregion

def upload_csv():
#region function
    """
    Takes the csv file made by make_csv() and uploads it to a specific folder on google drive
    """
    folder_id = '1UVCdt5k3SkpgTltZ0mogUcj4tpbz8-BN'
    upload_list = ['stock_data.csv']

    for upload_file in upload_list:
        gfile = drive.CreateFile({'parents': [{'id': folder_id}]})
        gfile.SetContentFile(upload_file)
        gfile.Upload()
#endregion


stock_data = get_data(ticker_list)

make_csv(stock_data)

upload_csv()