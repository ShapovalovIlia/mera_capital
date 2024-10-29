from mera_capital.application.gateways import CurrencyGateway
from mera_capital.application.models import Currency
from mera_capital.application.commands import GetCurrnecyRecordCommand


class GetCurrencyRecordProcessor:
    def __init__(
        self,
        currency_gateway: CurrencyGateway,
    ) -> None:
        self.currency_gateway = currency_gateway

    async def process(
        self, command: GetCurrnecyRecordCommand
    ) -> tuple[Currency, ...]:
        return await self.currency_gateway.from_interval(
            ticker=command.ticker, start=command.start, end=command.end
        )
