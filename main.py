from src.classAnalyzeFinanceData import AnalyzeFinanceData


if __name__ == "__main__":

    with AnalyzeFinanceData() as analyze_financeData:
        analyze_financeData.technicalIndicatorsCalcs()
        pass

