# import asyncio

# from typing import Annotated
# from fastapi import FastAPI, Depends, Query, HTTPException
# from uvicorn import Server, Config
# from sqlalchemy.ext.asyncio import create_async_engine

# from mera_capital.application import (
#     GetCurrencyRecordProcessor,
#     Ticker,
#     GetCurrnecyRecordCommand,
# )
# from mera_capital.infrastructure import (
#     CurrencyGatewayImpl,
#     postgres_config_from_env,
# )
# from mera_capital.presentation.stub import Stub


# app = FastAPI(title="Mera Capital")


# @app.get("/all_data/")
# async def all_data(
#     get_currency_record_processor: Annotated[GetCurrencyRecordProcessor, Depends(Stub(GetCurrencyRecordProcessor))],
#     ticker_query_param: str = Query(
#         ..., ticker="ticker"
#     ),  # Обязательный query-параметр
# ):
#     try:
#         ticker = Ticker(ticker_query_param)
#     except ValueError:
#         raise HTTPException(
#             status_code=412,
#             detail="There is no currency with such ticker in our data",
#         )

#     command = GetCurrnecyRecordCommand(ticker, start=None, end=None)
#     return await get_currency_record_processor.process(command)


# async def main() -> None:
#     config = Config(app, host="0.0.0.0")
#     server = Server(config)

#     db_engine = create_async_engine(postgres_config_from_env().url)
#     db_conn = db_engine.connect()
#     currency_gateway_impl = CurrencyGatewayImpl(connection=db_conn)
#     get_currency_record_processor = GetCurrencyRecordProcessor(
#         currency_gateway=currency_gateway_impl
#     )

#     app.dependency_overrides[Stub(GetCurrencyRecordProcessor)] = lambda: get_currency_record_processor

#     await server.serve()

# asyncio.run(main())
