import asyncio

from time import time
from uuid_extensions import uuid7

from mera_capital.application.constants import Ticker
from mera_capital.application.gateways import CurrencyGateway
from mera_capital.application.transaction_manager import TransactionManager
from mera_capital.application.client import DerebitClient
from mera_capital.application.commands import SyncCurrencyPriceCommand
from mera_capital.application.models import Currency
from mera_capital.application.value_objects import UnixTimestamp


class SyncCurrencyPriceProcessor:
    def __init__(
        self,
        *,
        currency_gateway: CurrencyGateway,
        transaction_manager: TransactionManager,
        derebit_client: DerebitClient,
    ) -> None:
        self.currency_gateway = currency_gateway
        self.transaction_manager = transaction_manager
        self.client = derebit_client

    async def process(
        self, sync_price_command: SyncCurrencyPriceCommand
    ) -> None:
        coros = [
            self._get_currency(ticker) for ticker in sync_price_command.tickers
        ]
        currencies = await asyncio.gather(*coros)
        await self.currency_gateway.save_many(currencies=currencies)
        await self.transaction_manager.commit()

    async def _get_currency(self, ticker: Ticker) -> Currency:
        curr_price = await self.client.current_index_price(ticker)
        return Currency(
            id=uuid7(),
            ticker=ticker,
            price=curr_price,
            created_at=UnixTimestamp(int(time())),
        )
