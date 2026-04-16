type Severity = "low" | "medium" | "high" | "critical";

interface EventRecord {
  eventId: string;
  source: string;
  eventType: string;
  severity: Severity;
  payload: Record<string, unknown>;
}

function shouldNotify(event: EventRecord, minimum: Severity): boolean {
  const order: Record<Severity, number> = { low: 0, medium: 1, high: 2, critical: 3 };
  return order[event.severity] >= order[minimum];
}

const event: EventRecord = {
  eventId: "sample-ts-001",
  source: "template",
  eventType: "sample.update",
  severity: "high",
  payload: { message: "template event" },
};

console.log({ shouldNotify: shouldNotify(event, "medium") });
