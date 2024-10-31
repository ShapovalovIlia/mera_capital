import asyncio

from uvicorn import Server, Config
from sqlalchemy.ext.asyncio import create_async_engine
from aiohttp import ClientSession

from mera_capital.infrastructure import (
    DerebitClientImpl,
    CurrencySynchronizer,
    postgres_config_from_env,
)
from mera_capital.presentation.web_api import app


async def run_web_api():
    config = Config(app, host="0.0.0.0")
    server = Server(config)
    await server.serve()


asyncio.run(run_web_api())


def run_currency_sync():
    engine = create_async_engine(postgres_config_from_env().url)

    session = ClientSession()
    derebit_cliet = DerebitClientImpl(session=session)
    synch = CurrencySynchronizer(derebit_client=derebit_cliet, engine=engine)
    synch.run()
