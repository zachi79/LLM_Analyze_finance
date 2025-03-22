from src.classAnalyzeFinanceData import AnalyzeFinanceData
from enum import Enum
import random
from src.utils.getListOfCompanies import getListOfCompanies


class RunningOptions(Enum):
    LEARNING = 1
    REGULAR = 2
    GUI = 3

Running = RunningOptions.LEARNING # choose the running option to run

def analyzeFinanceMain():
    with AnalyzeFinanceData() as analyze_financeData:
        analyze_financeData.technicalIndicatorsCalcs()
        pass

def learnAnalyzeFinance():

    '''
    instead default param need to add to get param from "user".
    in this case only the stock name change and saving data  (or running) for ML
    '''

    param = {"loadFinanceData":{}}
    table = {}
    sp500_tickers = getListOfCompanies()
    random.shuffle(sp500_tickers) #every time I will get diff list to learn and test

    # get the data and calc the indicators
    print("Start - get the data and calc the indicators")
    for tickers in sp500_tickers[0:50]:
        print(f"tickers: {tickers}")
        param["loadFinanceData"]["specificStock"] = [tickers]
        with AnalyzeFinanceData(param) as analyze_financeData:
            table[tickers] = analyze_financeData.technicalIndicatorsCalcs()
            pass
    print("Done - get the data and calc the indicators")
    # ML learn - 80% of the companies

    #ML test - 20% of the companies


if __name__ == "__main__":
    print("Starting...")
    # try:
    if Running == RunningOptions.LEARNING:
        learnAnalyzeFinance()
    elif Running == RunningOptions.REGULAR:
        # todo: Regullar analysis without gui - in progress
        analyzeFinanceMain()
        pass
    elif Running == RunningOptions.GUI:
        # todo: running analysis and adding GUI - not started
        pass
    else:
        raise Exception("Run option is not valid")
    # except Exception as err:
    #     print(f"Unexpected {err=}, {type(err)=}")
    #     pass
pass
