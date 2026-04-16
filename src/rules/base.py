from dataclasses import dataclass
from typing import Protocol

from src.event_schema import EventRecord


class Rule(Protocol):
    def evaluate(self, event: EventRecord) -> bool:
        ...


@dataclass(slots=True)
class SeverityAtLeastRule:
    minimum: str

    def evaluate(self, event: EventRecord) -> bool:
        order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        return order[event.severity] >= order[self.minimum]
