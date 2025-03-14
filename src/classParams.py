import json
from pydantic import BaseModel, Field, ValidationError
from models.paramModel import General, LoadFinanceDataData, GeneralModel, LoadFinanceDataModel,ParamsModel


class Params:
    def __init__(self):
        self.paramsFile = r"D:\learn\PythonProject\LLM_Analyze_finance\financeParams.json"
        self.params = self.load_params_from_json(self.paramsFile)
        pass

    def __enter__(self):
        # the enter auto call when it calls with "with".
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def load_params_from_json(self, file_path: str):
        try:
            with open(file_path, 'r') as file:
                raw_params = json.load(file)

            # Validate each section separately using Pydantic
            general_validated = GeneralModel(**raw_params.get("general", {}))
            load_finance_data_validated = LoadFinanceDataModel(**raw_params.get("loadFinanceData", {}))

            # Convert Pydantic models to dataclasses
            general_data = General(useS3=general_validated.useS3)
            load_finance_data_data = LoadFinanceDataData(
                useSpecificStocks=load_finance_data_validated.useSpecificStocks,
                specificStocks=load_finance_data_validated.specificStocks,
                reloadData=load_finance_data_validated.reloadData,
                startDate=load_finance_data_validated.startDate,
                endDate=load_finance_data_validated.endDate
            )

            return ParamsModel(general=general_data, loadFinanceData=load_finance_data_data)

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f" Error reading param file: {e}")
            raise

        except ValidationError as e:
            print(f" Parameter validation failed:\n{e}")
            raise

        except Exception  as e:
            print(f"Unexpected error occurred: {e}")
            raise