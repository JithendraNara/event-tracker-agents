from src.event_schema import EventRecord, validate_event


def test_validate_event_accepts_valid_record() -> None:
    record = EventRecord(
        event_id="ok-1",
        source="unit-test",
        event_type="test.event",
        severity="low",
    )
    validate_event(record)
