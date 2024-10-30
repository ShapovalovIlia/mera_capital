from dataclasses import dataclass

from mera_capital.application.constants import Ticker


@dataclass(frozen=True, slots=True)
class SyncCurrPriceCommand:
    ticker: Ticker
