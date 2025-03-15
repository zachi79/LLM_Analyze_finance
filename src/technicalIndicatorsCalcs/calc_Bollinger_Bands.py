import ta

'''
Bollinger Bands consist of three lines:

Middle Band (SMA) → Simple Moving Average (SMA)
Upper Band → SMA + (Standard Deviation * multiplier)
Lower Band → SMA - (Standard Deviation * multiplier)
The default window is 20 days, and the standard deviation multiplier is 2.

How to Interpret Bollinger Bands?
Price Touches Upper Band → Overbought (Possible Sell Signal)
Price Touches Lower Band → Oversold (Possible Buy Signal)
Bands Widen → Higher Volatility
Bands Contract (Squeeze) → Low Volatility, Potential Breakout

How to Choose?
For daily data (~125 days):
    window=20 (Default) is still a good choice.
    Use window=30 for smoother trends.
    Keep window_dev=2.0 for balanced volatility detection.
For weekly data (~26 weeks):
    Use window=10-15, since 26 weeks is not a large dataset.
    Use window_dev=2.0 to 2.5 to capture longer trends.
For monthly data (~6 months):
    Use window=5-10 to avoid too much lag.
    Use window_dev=2.5 to 3.0 for stronger volatility confirmation.

'''
def calc_Bollinger_Bands(data,params):
    bollinger_Bands_window = params.technicalIndicators.bollingerBandsWindow
    bollinger_Bands_window_dev = params.technicalIndicators.bollingerBandsWindowDev

    bb = ta.volatility.BollingerBands(close=data['Close'],
                                      window=int(bollinger_Bands_window),
                                      window_dev=bollinger_Bands_window_dev)

    # Add Bollinger Bands to DataFrame
    data['Bollinger_Bands_SMA'] = bb.bollinger_mavg()
    data['Bollinger_Bands_Upper_Band'] = bb.bollinger_hband()
    data['Bollinger_Bands_Lower_Band'] = bb.bollinger_lband()

    return data