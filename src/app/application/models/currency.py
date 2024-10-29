from app.application.constants import Ticker
from app.application.value_objects import UnixTimestamp


class Currency:
    def __init__(
        self, *, ticker: Ticker, price: float, time: UnixTimestamp
    ) -> None:
        self.ticker = ticker
        self.price = price
        self.time = time

    @classmethod
    def create(
        cls, ticker: Ticker, price: float, time: UnixTimestamp
    ) -> "Currency":
        return Currency(ticker=ticker, price=price, time=time)
