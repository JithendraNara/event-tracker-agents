from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Literal

Severity = Literal["low", "medium", "high", "critical"]


@dataclass(slots=True)
class EventRecord:
    event_id: str
    source: str
    event_type: str
    severity: Severity
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    payload: Dict[str, Any] = field(default_factory=dict)


def validate_event(record: EventRecord) -> None:
    if not record.event_id.strip():
        raise ValueError("event_id is required")
    if not record.source.strip():
        raise ValueError("source is required")
    if not record.event_type.strip():
        raise ValueError("event_type is required")
