from dataclasses import dataclass
from typing import Iterable

from mera_capital.application.constants import Ticker


@dataclass(frozen=True, slots=True)
class SyncCurrencyPriceCommand:
    tickers: Iterable[Ticker]
