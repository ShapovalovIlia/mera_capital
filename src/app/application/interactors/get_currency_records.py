from app.application.gateways import CurrencyGateway
from app.application.models import Currency
from app.application.commands import GetCurrnecyRecordCommand


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
