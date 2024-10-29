from uuid import UUID

from mera_capital.application.constants import Ticker
from mera_capital.application.value_objects import UnixTimestamp


class Currency:
    def __init__(
        self, *, id: UUID, ticker: Ticker, price: float, time: UnixTimestamp
    ) -> None:
        self.id = id
        self.ticker = ticker
        self.price = price
        self.time = time

    @classmethod
    def create(
        cls, *, id: UUID, ticker: Ticker, price: float, time: UnixTimestamp
    ) -> "Currency":
        return Currency(id=id, ticker=ticker, price=price, time=time)
