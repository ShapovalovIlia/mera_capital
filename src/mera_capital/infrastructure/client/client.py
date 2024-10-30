import aiohttp
from mera_capital.application.constants import Ticker


class ClientImpl:
    async def current_index_price(self, ticker: Ticker) -> float:
        url = f"https://test.deribit.com/api/v2/public/get_index_price?index_name={ticker.value}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                data = await response.json()
                return data["result"]["index_price"]
