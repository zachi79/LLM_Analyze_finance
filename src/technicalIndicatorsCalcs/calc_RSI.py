import ta
'''
from the internet/chatgpt

The Relative Strength Index (RSI) is a momentum oscillator that measures 
the speed and change of price movements. It ranges from 0 to 100, with values above 70
indicating overbought conditions and below 30 indicating oversold conditions.


Formula for RSI:
Calculate the price change: Gain=max⁡(Price Change,0)\text{Gain} = \max(\text{Price Change}, 0)Gain=max(Price Change,0) Loss=max⁡(−Price Change,0)\text{Loss} = \max(-\text{Price Change}, 0)Loss=max(−Price Change,0)
Compute the average gain and loss using an exponential moving average (EMA): RS=Average GainAverage Loss\text{RS} = \frac{\text{Average Gain}}{\text{Average Loss}}RS=Average LossAverage Gain​
Calculate RSI: RSI=100−(1001+RS)RSI = 100 - \left(\frac{100}{1 + RS}\right)RSI=100−(1+RS100​)


Why window 14?
Balanced Sensitivity:

Shorter periods (e.g., 7 or 9) make RSI more sensitive, leading to more frequent overbought/oversold signals.
Longer periods (e.g., 21 or 30) make RSI smoother, reducing false signals.
14 is a balanced choice, commonly used by traders.

for 2 years:
data['RSI_50'] = calculate_rsi(data, window=50)  # For long-term trend analysis
data['RSI_100'] = calculate_rsi(data, window=100)  # Even smoother for 2-year data

for 6 month
data['RSI_20'] = calculate_rsi(data, window=20)  # Balanced for 6-month trends
data['RSI_30'] = calculate_rsi(data, window=30)  # Smoother trend tracking

for 1-2 month
data['RSI_7'] = calculate_rsi(data, window=7)   # Faster signal
data['RSI_14'] = calculate_rsi(data, window=14)  # Standard short-term RSI

'''
def calc1RSI(data, param):

    delta = data['Close'].diff(1)  # Price difference

    gain = (delta.where(delta > 0, 0))  # Keep gains, set losses to 0
    loss = (-delta.where(delta < 0, 0))  # Keep losses, set gains to 0

    avg_gain = gain.rolling(window=param.technicalIndicators.rsiWindow, min_periods=1).mean()
    avg_loss = loss.rolling(window=param.technicalIndicators.rsiWindow, min_periods=1).mean()

    rs = avg_gain / avg_loss  # Relative Strength
    rsi = 100 - (100 / (1 + rs))  # RSI formula

    return rsi


def calc2RSI(data, param):
    rsi = ta.momentum.RSIIndicator(close=data['Close'], window=param.technicalIndicators.rsiWindow).rsi()
    return rsi

def calc_RSI(data, param):
    c1RSI = calc1RSI(data, param)
    # c2RSI = calc2RSI(data, param) # another solution but need to change the Data for this. TBD
    return c1RSI