from typing import Protocol

from mera_capital.application.constants import Ticker


class IClient(Protocol):
    async def current_index_price(self, ticker: Ticker) -> float:
        raise NotImplementedError
