import ta

'''
The Moving Average Convergence Divergence (MACD) is a momentum indicator that
shows the relationship between two moving averages of a stock's price.
It consists of three components:

1. MACD Line = EMA(12) - EMA(26) (Difference between short-term and long-term EMAs)
2. Signal Line = 9-day EMA of MACD Line (Used to generate buy/sell signals)
3. MACD Histogram = MACD Line - Signal Line (Shows momentum strength)

How to Interpret MACD?
MACD Line crosses above Signal Line → Bullish signal (Buy)
MACD Line crosses below Signal Line → Bearish signal (Sell)
MACD Histogram positive & increasing → Strong upward momentum
MACD Histogram negative & decreasing → Strong downward momentum

'''

def calc_MACD(data, params):
    short_window = params.technicalIndicators.macdShortWindow
    long_window = params.technicalIndicators.macdLongWindow
    signal_window = params.technicalIndicators.macdSignalWindow
    macd = ta.trend.MACD(close=data['Close'],
                         window_slow=short_window,
                         window_fast=long_window,
                         window_sign=signal_window)
    data['MACD_Line'] = macd.macd()
    data['MACD_Signal_Line'] = macd.macd_signal()
    data['MACD_Histogram'] = macd.macd_diff()
    return data

