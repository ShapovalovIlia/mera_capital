from typing import Protocol

from mera_capital.application.models.currency import Currency
from mera_capital.application.constants import Ticker
from mera_capital.application.value_objects import UnixTimestamp


class CurrencyGateway(Protocol):
    async def save(self, currency: Currency) -> None:
        raise NotImplementedError

    async def from_interval(
        self,
        *,
        ticker: Ticker,
        start: UnixTimestamp | None,
        end: UnixTimestamp | None,
    ) -> tuple[Currency, ...]:
        raise NotImplementedError
