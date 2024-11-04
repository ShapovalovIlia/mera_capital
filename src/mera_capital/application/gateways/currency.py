from typing import Protocol

from mera_capital.application.models import Currency
from mera_capital.application.constants import Ticker
from mera_capital.application.value_objects import UnixTimestamp


class CurrencyGateway(Protocol):
    async def save(self, currency: Currency) -> None:
        raise NotImplementedError

    async def save_many(self, currencies: list[Currency]) -> None:
        raise NotImplementedError

    async def by_interval(
        self,
        *,
        ticker: Ticker,
        start: UnixTimestamp | None,
        end: UnixTimestamp | None,
    ) -> list[Currency]:
        raise NotImplementedError
