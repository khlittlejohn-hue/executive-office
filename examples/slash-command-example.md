# /brief: daily cross-department brief

An example slash command, sanitized. It shows how the system packages a multi-step, multi-agent workflow behind a single repeatable entry point.

## What it does
1. Reads each department's status file (current state, blockers, next actions).
2. Dispatches a summarizer agent per department in parallel.
3. Aggregates the summaries into one ranked brief: what changed, what needs a decision today, and what is blocked.
4. Renders the brief to an HTML view and surfaces the top decisions for approval.

## Usage
- `/brief`, full brief, archived to history.
- `/brief status`, snapshot only, no archive.

## Design notes
- Single-writer: only this command writes the daily brief file, which prevents state drift across the system.
- Read-only on source data: it summarizes department state, it does not mutate it.
- Human-in-the-loop: decisions are surfaced for approval and never actioned automatically.
- Parallel fan-out: department summarizers run concurrently, so wall-clock time is the slowest single summary, not the sum.
