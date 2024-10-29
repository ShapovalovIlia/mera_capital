from dataclasses import dataclass

from app.application.value_objects import UnixTimestamp
from app.application.constants import Ticker


@dataclass(frozen=True, slots=True)
class GetCurrnecyRecordCommand:
    ticker: Ticker
    start: UnixTimestamp | None
    end: UnixTimestamp | None
