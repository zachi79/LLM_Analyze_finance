from src.classGetFinanceData import GetFinanceData
from src.technicalIndicatorsCalcs.calc_Bollinger_Bands import calc_Bollinger_Bands
from src.technicalIndicatorsCalcs.calc_MACD import calc_MACD
from src.technicalIndicatorsCalcs.calc_RSI import calc_RSI
from src.technicalIndicatorsCalcs.calc_SMA_EMA import calc_SMA_EMA


class AnalyzeFinanceData(GetFinanceData):
    def __init__(self):
        super().__init__()

        pass


    def technicalIndicatorsCalcs(self):
        """
        ממוצעים נעים (SMA, EMA)
        אינדיקטור מומנטום (RSI)
        מתנד MACD
        סטיות תקן (Bollinger Bands)

        :return: Indicators Calcs
        """
        self.calcSMA, self.calcEMA = calc_SMA_EMA(self.data, self.params)
        self.calcRSI = calc_RSI(self.data, self.params)
        self.calcMACD = calc_MACD(self.data, self.params)
        self.calcBollingerBands = calc_Bollinger_Bands(self.data, self.params)
        pass
