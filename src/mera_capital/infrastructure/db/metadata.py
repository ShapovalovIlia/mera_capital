from sqlalchemy import Column, MetaData, Table, UUID, Float, Integer
from sqlalchemy.dialects import postgresql

from mera_capital.application.constants import Ticker

metadata = MetaData()

currnecy_table = Table(
    "currencies",
    metadata,
    Column("id", primary_key=True, type_=UUID),
    Column("ticker", postgresql.ENUM(Ticker)),
    Column("price", type_=Float),
    Column("created_at", type_=Integer),
)
