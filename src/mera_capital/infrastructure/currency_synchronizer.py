import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine

from mera_capital.application import (
    SyncCurrencyPriceProcessor,
    Ticker,
    SyncCurrencyPriceCommand,
)
from mera_capital.infrastructure.db.gateways_impl import CurrencyGatewayImpl
from mera_capital.infrastructure.clients import DerebitClientImpl


class CurrencySynchronizer:
    def __init__(
        self, derebit_client: DerebitClientImpl, engine: AsyncEngine
    ) -> None:
        self.derebit_client = derebit_client
        self.engine = engine

    async def run(self):
        while True:
            conn = self.engine.connect()
            gateway = CurrencyGatewayImpl(conn)

            command_processor = SyncCurrencyPriceProcessor(
                currency_gateway=gateway,
                transaction_manager=conn,
                derebit_client=self.derebit_client,
            )
            command = SyncCurrencyPriceCommand([Ticker.BTC, Ticker.ETH])
            await command_processor.process(sync_price_command=command)
            await asyncio.sleep(60)
