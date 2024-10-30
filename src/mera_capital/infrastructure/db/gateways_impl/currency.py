from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from sqlalchemy import select

from mera_capital.application.models import Currency
from mera_capital.infrastructure.db.metadata import currnecy_table
from mera_capital.application.constants import Ticker
from mera_capital.application.value_objects import UnixTimestamp


class CurrencyGatewayImpl:
    def __init__(self, connection: AsyncSession):
        self._connection = connection

    async def save(self, currency: Currency):
        stmt = insert(currnecy_table).values(
            id=currency.id,
            ticker=currency.ticker,
            price=currency.price,
            created_at=currency.created_at,
        )
        async with self._connection.begin() as transaction:
            await self._connection.execute(stmt)
            await transaction.commit()

    async def from_interval(
        self,
        *,
        ticker: Ticker,
        start: UnixTimestamp,
        end: UnixTimestamp,
    ) -> tuple[Currency, ...]:
        query = select(currnecy_table).where(currnecy_table.c.ticker == ticker)

        if start is not None:
            query = query.where(currnecy_table.c.created_at >= start)

        if end is not None:
            query = query.where(currnecy_table.c.created_at <= end)

        result = await self._connection.execute(query)
        return tuple(result.scalars().all())
