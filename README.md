# event-tracker-agents

Unified event and monitoring agent templates for sports, policy, and operational alerting workflows.

## Why this repository exists

This repository consolidates multiple one-off `gear-*` tracker projects into a single, reusable foundation so future trackers share:

- common ingestion patterns
- common alerting interfaces
- shared deployment and operations guidance
- consistent testing and observability standards

## Architecture at a glance

1. **Source adapters** pull data from APIs, feeds, or pages.
2. **Normalization layer** converts raw events into a common event schema.
3. **Rules engine** evaluates event conditions and trigger logic.
4. **Notification layer** routes alerts to configured channels.
5. **Storage/telemetry** records event history, status, and health metrics.

## Repository layout

```text
.
├── docs/
│   ├── ARCHITECTURE.md
│   └── MIGRATION_MAP.md
├── templates/
│   ├── tracker-template-python/
│   └── tracker-template-typescript/
├── examples/
│   ├── sports/
│   ├── policy/
│   └── ops/
└── src/
    ├── adapters/
    ├── rules/
    └── notifiers/
```

## Migration map

Legacy repos were archived and redirected here (for example: sports live trackers, policy watchers, and state-change monitors).

Use `docs/MIGRATION_MAP.md` to map old repository names to their new module families.

## Getting started

1. Choose a template in `templates/`.
2. Implement source adapter(s) in `src/adapters/`.
3. Add rules in `src/rules/`.
4. Configure notifier(s) in `src/notifiers/`.
5. Add an example under `examples/` and validate with local tests.

## Roadmap

- [ ] Publish canonical event schema (`v1`)
- [ ] Add template CLI scaffolder
- [ ] Add pluggable notifier registry
- [ ] Add basic replay simulator for backtesting rules

## Contribution standard

Every new tracker module should include:

- a short architecture note
- local run instructions
- test coverage for rule evaluation
- a migration note if replacing legacy behavior
