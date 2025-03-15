
import pandas as pd

def calculate_sma(data, window):
    return data['Close'].rolling(window=window).mean()

def calculate_ema(data, window):
    return data['Close'].ewm(span=window, adjust=False).mean()

def calc_SMA_EMA(data, params):
    """
    calc the EMA and SMA for the close data in the stock
    :param data: dataframe
    :return: EMA and SMA
    """
    calcSMA = calculate_sma(data, params.technicalIndicators.smaWindow)
    calcEMA = calculate_ema(data, params.technicalIndicators.emaWindow)
    return calcSMA, calcEMA
