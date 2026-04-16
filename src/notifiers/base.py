from abc import ABC, abstractmethod

from src.event_schema import EventRecord


class Notifier(ABC):
    name: str

    @abstractmethod
    def send(self, event: EventRecord) -> None:
        """Send an event to an output channel."""
