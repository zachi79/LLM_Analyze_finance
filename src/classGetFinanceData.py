import yfinance as yf
import pandas as pd
import pickle
import os
from src.classParams import Params


class GetFinanceData(Params):
    def __init__(self):
        super().__init__()
        if self.params.loadFinanceData.useSpecificStocks == True:
            self.data = self.get_data_specific()
        else:
            self.data = self.get_data()
        pass

    def __enter__(self):


        return self  # This is necessary for 'with' to work properly

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_data(self):
        print("Fetching financial data...")
        '''
        📌 שלב 1: איסוף נתונים פיננסיים
        שימוש ב-Yahoo Finance API או Binance API (לקריפטו) לשליפת מחירים היסטוריים (Open, High, Low, Close, Volume).
        אחסון הנתונים כ-DataFrame ב-Pandas.
        '''
        if (os.path.exists("../sp500_data.pkl") and
                self.params.loadFinanceData.reloadData==False):
            with open("../sp500_data.pkl", "rb") as f:
                sp500_data = pickle.load(f)
        else:
            url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
            sp500_tickers = pd.read_html(url)[0]['Symbol'].tolist()

            # Download historical market data for S&P 500 stocks
            sp500_data = {}

            for ticker in sp500_tickers:  # Limit to 5 stocks for testing
                stock = yf.Ticker(ticker)
                sp500_data[ticker] = stock.history(start=self.params.loadFinanceData.startDate,
                                                   end=self.params.loadFinanceData.endDate)
            with open("../sp500_data.pkl", "wb") as f:
                pickle.dump(sp500_data, f)

    def get_data_specific(self):
        tickers = self.params.loadFinanceData.specificStocks

        # Download hourly data
        data = {ticker: yf.download(ticker, period="30d", interval="1h") for ticker in tickers}

        return data

