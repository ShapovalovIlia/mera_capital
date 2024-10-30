from time import time
from uuid_extensions import uuid7

from mera_capital.application.gateways import CurrencyGateway
from mera_capital.application.transaction_manager import TransactionManager
from mera_capital.application.client import IClient
from mera_capital.application.commands import SyncCurrPriceCommand
from mera_capital.application.models import Currency
from mera_capital.application.value_objects import UnixTimestamp


class SyncCurrPriceProcessor:
    def __init__(
        self,
        currency_gateway: CurrencyGateway,
        transaction_manager: TransactionManager,
        client: IClient,
    ) -> None:
        self.currency_gateway = currency_gateway
        self.transaction_manager = transaction_manager
        self.client = client

    async def process(self, sync_price_command: SyncCurrPriceCommand) -> None:
        price = await self.client.current_index_price(
            sync_price_command.ticker
        )
        curr_time = UnixTimestamp(int(time()))
        currency = Currency.create(
            id=uuid7(),
            ticker=sync_price_command.ticker,
            price=price,
            created_at=curr_time,
        )
        await self.currency_gateway.save(currency)
        await self.transaction_manager.commit()
