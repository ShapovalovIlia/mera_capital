from typing import Protocol

from app.application.models import Currency
from app.application.constants import Ticker
from app.application.value_objects import UnixTimestamp


class CurrencyGateway(Protocol):
    async def save(self, currency: Currency) -> None:
        raise NotImplementedError

    async def from_interval(
        self,
        *,
        ticker: Ticker,
        start: UnixTimestamp | None,
        end: UnixTimestamp | None,
    ) -> tuple[Ticker, ...]:
        raise NotImplementedError
