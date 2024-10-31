import asyncio

from fastapi import FastAPI, Depends
from uvicorn import Server, Config

from mera_capital.application import (
    GetCurrencyRecordProcessor,
    Ticker,
    GetCurrnecyRecordCommand,
)

from mera_capital.infrastructure import (
    CurrencyGatewayImpl,
    postgres_config_from_env,
)

from sqlalchemy.ext.asyncio import create_async_engine

app = FastAPI(title="Mera Capital")


@app.get("/all_data/{ticker}")
async def all_data(
    ticker: Ticker,
    get_currency_record_processor: GetCurrencyRecordProcessor = Depends(),
):
    command = GetCurrnecyRecordCommand(ticker, start=None, end=None)
    return await get_currency_record_processor.process(command)


async def main() -> None:
    config = Config(app, host="0.0.0.0")
    server = Server(config)

    engine = create_async_engine(postgres_config_from_env().url)
    conn = engine.connect()
    currency_gateway_impl = CurrencyGatewayImpl(connection=conn)
    get_currency_record_processor = GetCurrencyRecordProcessor(
        currency_gateway=currency_gateway_impl
    )
    app.dependency_overrides[GetCurrencyRecordProcessor] = (
        lambda: get_currency_record_processor
    )

    await server.serve()


asyncio.run(main())
