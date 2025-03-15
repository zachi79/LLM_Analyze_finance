from dataclasses import dataclass
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

# Define Pydantic model for loadFinanceData
class LoadFinanceDataModel(BaseModel):
    useSpecificStocks: bool = Field(default=True, description="Whether to use specific stocks")
    specificStock: List[str] = Field(default=False, description="List of specific stocks")
    reloadData: bool = Field(default=False, description="Whether to reload the data")
    startDate: str = Field(default=False, description="Start date for fetching data")
    endDate: str = Field(default=False, description="End date for fetching data")

class GeneralModel(BaseModel):
    useS3: bool = Field(default=False, description="Whether to use AWS S3")

class TechnicalIndicatorsModel(BaseModel):
    smaWindow: float = Field(default=False, description="SMA indicator Window")
    emaWindow: float = Field(default=False, description="EMA indicator Window")
    rsiWindow: float = Field(default=False, description="RSI indicator Window")
    macdShortWindow: float = Field(default=False, description="MACD indicator Short Window")
    macdLongWindow: float = Field(default=False, description="MACD indicator Long Window")
    macdSignalWindow: float = Field(default=False, description="MACD indicator Signal Window")
    bollingerBandsWindow: float = Field(default=False, description="Bollinger Bands indicator Window")
    bollingerBandsWindowDev: float = Field(default=False, description="Bollinger Bands indicator Window Dev")


#  Define dataclass to store validated parameters
@dataclass
class LoadFinanceDataData:
    useSpecificStocks: bool
    specificStock: List[str]
    reloadData: bool
    startDate: str
    endDate: str

@dataclass
class General:
    useS3: bool


@dataclass
class TechnicalIndicators:
    smaWindow: float
    emaWindow: float
    rsiWindow: float
    macdShortWindow: float
    macdLongWindow: float
    macdSignalWindow: float
    bollingerBandsWindow: float
    bollingerBandsWindowDev: float

@dataclass
class ParamsModel:
    general: General
    loadFinanceData: LoadFinanceDataData
    technicalIndicators: TechnicalIndicators
