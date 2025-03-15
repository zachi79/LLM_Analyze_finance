import ta

def calculate_sma(data, SMAWindow):
    sma_indicator = ta.trend.SMAIndicator(close=data['Close'], window=int(SMAWindow))
    data['SMA_20'] = sma_indicator.sma_indicator()
    return data

def calculate_ema(data, EMAWindow):
    ema_indicator = ta.trend.EMAIndicator(close=data['Close'], window=int(EMAWindow))
    data['EMA_20'] = ema_indicator.ema_indicator()
    return data


def calc_SMA_EMA(data, params):
    """
    calc the EMA and SMA for the close data in the stock
    :param data: dataframe
    :return: EMA and SMA
    """
    calcSMA = calculate_sma(data, params.technicalIndicators.smaWindow)
    calcEMA = calculate_ema(data, params.technicalIndicators.emaWindow)
    return calcSMA, calcEMA
