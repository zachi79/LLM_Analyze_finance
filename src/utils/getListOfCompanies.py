import pandas as pd

def getListOfCompanies():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    sp500_tickers = pd.read_html(url)[0]['Symbol'].tolist()
    return sp500_tickers
