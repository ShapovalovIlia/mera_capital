from aiohttp import ClientSession

from mera_capital.application import Ticker


class DerebitClientImpl:
    def __init__(self, session: ClientSession) -> None:
        self._session = session

    async def current_index_price(self, ticker: Ticker) -> float:
        url = f"https://test.deribit.com/api/v2/public/get_index_price?index_name={ticker.value}"
        async with self._session.get(url, ssl=False) as response:
            data = await response.json()
            return data["result"]["index_price"]
