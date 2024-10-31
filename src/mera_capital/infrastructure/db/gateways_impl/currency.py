from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy import insert, select

from mera_capital.application import Currency, Ticker, UnixTimestamp
from mera_capital.infrastructure.db.metadata import currnecy_table


class CurrencyGatewayImpl:
    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    async def save(self, currency: Currency) -> None:
        stmt = insert(currnecy_table).values(
            id=currency.id,
            ticker=currency.ticker,
            price=currency.price,
            created_at=currency.created_at,
        )
        await self._connection.execute(stmt)

    async def save_many(self, currencies: list[Currency]) -> None:
        stmt = insert(currnecy_table).values(
            [
                {
                    "id": currency.id,
                    "ticker": currency.ticker,
                    "price": currency.price,
                    "created_at": currency.created_at,
                }
                for currency in currencies
            ]
        )
        await self._connection.execute(stmt)

    async def by_interval(
        self,
        *,
        ticker: Ticker,
        start: UnixTimestamp | None,
        end: UnixTimestamp | None,
    ) -> list[Currency]:
        query = select(currnecy_table).where(currnecy_table.c.ticker == ticker)

        if start is not None:
            query = query.where(currnecy_table.c.created_at >= start)

        if end is not None:
            query = query.where(currnecy_table.c.created_at <= end)

        result = await self._connection.execute(query)
        return list(result.scalars().all())
