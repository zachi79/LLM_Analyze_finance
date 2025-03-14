from dataclasses import dataclass
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

# Define Pydantic model for loadFinanceData
class LoadFinanceDataModel(BaseModel):
    useSpecificStocks: bool = Field(default=True, description="Whether to use specific stocks")
    specificStocks: List[str] = Field(default=False, description="List of specific stocks")
    reloadData: bool = Field(default=False, description="Whether to reload the data")
    startDate: str = Field(default=False, description="Start date for fetching data")
    endDate: str = Field(default=False, description="End date for fetching data")

class GeneralModel(BaseModel):
    useS3: bool = Field(default=False, description="Whether to use AWS S3")

#  Define dataclass to store validated parameters
@dataclass
class LoadFinanceDataData:
    useSpecificStocks: bool
    specificStocks: List[str]
    reloadData: bool
    startDate: str
    endDate: str

@dataclass
class General:
    useS3: bool

@dataclass
class ParamsModel:
    general: General
    loadFinanceData: LoadFinanceDataData
