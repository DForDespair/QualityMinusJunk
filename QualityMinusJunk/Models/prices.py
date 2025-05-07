from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Price:
    open: float
    high: float
    low: float
    close: float
    volume: float
    timestamp: datetime

@dataclass    
class PriceHistory:
    prices: List[Price]