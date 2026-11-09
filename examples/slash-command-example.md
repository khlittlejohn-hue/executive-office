# /brief: daily cross-department brief

> **Example type: template.** A sanitized description of a real command's shape, not its full private definition.

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
- One writer, two entry points: the command does not write the brief itself. It invokes the Chief of Staff agent in brief mode, the same writer a [scheduled task](./scheduled-task-example.md) would invoke. One owner of the file prevents state drift; there is no file lock, so this is a design convention, not a concurrency guarantee.
- Read-only on source data: it summarizes department state, it does not mutate it.
- Human-in-the-loop: decisions are surfaced for approval and never actioned automatically.
- Parallel fan-out: department summarizers run concurrently, so wall-clock time is the slowest single summary, not the sum.
