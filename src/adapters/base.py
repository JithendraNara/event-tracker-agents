from abc import ABC, abstractmethod
from typing import Iterable

from src.event_schema import EventRecord


class SourceAdapter(ABC):
    name: str

    @abstractmethod
    def fetch(self) -> Iterable[EventRecord]:
        """Return normalized event records from a source."""
