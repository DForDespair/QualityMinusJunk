from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from datetime import datetime
from typing import List, Optional
from enum import Enum
from QualityMinusJunk.Models.fundamentals import BalanceSheet, CashFlowStatement, FundamentalSnapshot, IncomeStatement
from QualityMinusJunk.Models.prices import Price, PriceHistory




@dataclass
class Security:
    ticker_root: str
    ticker_suffix: str
    ticker: str = field(init=False)   
    isActive: bool
    delisted_utc: Optional[datetime]
    list_date: datetime
    locale: str
    def __post_init__(self):
        self.ticker = self.ticker_root + self.ticker_suffix
    
@dataclass 
class Stock(Security):
   exchange: Optional[str] = None
   currency: Optional[str] = None
   daily_prices: PriceHistory = field(default_factory=PriceHistory)
   
@dataclass
class Company:
    company_name: str
    cik: str
    sic: str
    securities: List[Security]
    fundamentals: List[FundamentalSnapshot]

    