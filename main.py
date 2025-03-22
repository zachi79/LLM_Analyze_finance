from src.classAnalyzeFinanceData import AnalyzeFinanceData
from enum import Enum

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
    sp500_tickers = getListOfCompanies()
    for tickers in sp500_tickers:
        param["loadFinanceData"]["specificStock"] = [tickers]
        with AnalyzeFinanceData(param) as analyze_financeData:
            analyze_financeData.technicalIndicatorsCalcs()
            pass



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
