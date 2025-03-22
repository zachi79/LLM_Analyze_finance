import json
from pydantic import BaseModel, Field, ValidationError
from models.paramModel import General, LoadFinanceDataData, GeneralModel, LoadFinanceDataModel, ParamsModel, \
    TechnicalIndicatorsModel, TechnicalIndicators


class Params:
    def __init__(self, param):
        self.paramsFile = r"D:\learn\PythonProject\LLM_Analyze_finance\financeParams.json"
        self.params = self.load_params_from_json(self.paramsFile)
        self.update_params_model(param)
        pass

    def __enter__(self):
        # the enter auto call when it calls with "with".
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def update_params_model(self, update_dict: dict) -> ParamsModel:
        """Updates a ParamsModel dataclass with values from a dictionary."""

        for key, value in update_dict.items():
            if hasattr(self.params, key):
                field_type = type(getattr(self.params, key))
                if isinstance(value, dict) and field_type.__name__ == type(getattr(self.params, key)).__name__:
                    # Recursively update nested dataclasses
                    nested_dataclass = getattr(self.params, key)
                    for nested_key, nested_value in value.items():
                        if hasattr(nested_dataclass, nested_key):
                            setattr(nested_dataclass, nested_key, nested_value)
                else:
                    setattr(self.params, key, value)
        return self.params


    def load_params_from_json(self, file_path: str):
        try:
            with open(file_path, 'r') as file:
                raw_params = json.load(file)

            # Validate each section separately using Pydantic
            general_validated = GeneralModel(**raw_params.get("general", {}))
            load_finance_data_validated = LoadFinanceDataModel(**raw_params.get("loadFinanceData", {}))
            technical_indicators_validated = TechnicalIndicatorsModel(**raw_params.get("technicalIndicatorsCalcs", {}))

            # Convert Pydantic models to dataclasses
            general_data = General(useS3=general_validated.useS3)
            load_finance_data_data = LoadFinanceDataData(
                useSpecificStocks=load_finance_data_validated.useSpecificStocks,
                specificStock=load_finance_data_validated.specificStock,
                reloadData=load_finance_data_validated.reloadData,
                startDate=load_finance_data_validated.startDate,
                endDate=load_finance_data_validated.endDate
            )
            technical_indicators_data = TechnicalIndicators(smaWindow=technical_indicators_validated.smaWindow,
                                                            emaWindow=technical_indicators_validated.emaWindow,
                                                            rsiWindow=technical_indicators_validated.rsiWindow,
                                                            macdShortWindow=technical_indicators_validated.macdShortWindow,
                                                            macdLongWindow=technical_indicators_validated.macdLongWindow,
                                                            macdSignalWindow=technical_indicators_validated.macdSignalWindow,
                                                            bollingerBandsWindow=technical_indicators_validated.bollingerBandsWindow,
                                                            bollingerBandsWindowDev=technical_indicators_validated.bollingerBandsWindowDev

                                                            )

            return ParamsModel(general=general_data,
                               loadFinanceData=load_finance_data_data,
                               technicalIndicators = technical_indicators_data
                               )

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f" Error reading param file: {e}")
            raise

        except ValidationError as e:
            print(f" Parameter validation failed:\n{e}")
            raise

        except Exception  as e:
            print(f"Unexpected error occurred: {e}")
            raise