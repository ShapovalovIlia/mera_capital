from uuid import UUID

from mera_capital.application.constants import Ticker
from mera_capital.application.value_objects import UnixTimestamp


class Currency:
    def __init__(
        self,
        *,
        id: UUID,
        ticker: Ticker,
        price: float,
        created_at: UnixTimestamp,
    ) -> None:
        self.id = id
        self.ticker = ticker
        self.price = price
        self.created_at = created_at

    @classmethod
    def create(
        cls,
        *,
        id: UUID,
        ticker: Ticker,
        price: float,
        created_at: UnixTimestamp,
    ) -> "Currency":
        return Currency(
            id=id, ticker=ticker, price=price, created_at=created_at
        )
