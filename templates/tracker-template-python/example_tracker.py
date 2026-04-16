from src.event_schema import EventRecord, validate_event
from src.rules.base import SeverityAtLeastRule


def run_sample() -> bool:
    event = EventRecord(
        event_id="sample-001",
        source="template",
        event_type="sample.update",
        severity="high",
        payload={"message": "template event"},
    )
    validate_event(event)
    return SeverityAtLeastRule(minimum="medium").evaluate(event)


if __name__ == "__main__":
    print({"should_notify": run_sample()})
