from dataclasses import dataclass

from mera_capital.application.value_objects import UnixTimestamp
from mera_capital.application.constants import Ticker


@dataclass(frozen=True, slots=True)
class GetCurrnecyRecordCommand:
    ticker: Ticker
    start: UnixTimestamp | None
    end: UnixTimestamp | None
