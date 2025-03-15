from src.classGetFinanceData import GetFinanceData
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

        pass
