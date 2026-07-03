# Scheduled task: the morning brief

An example of a recurring scheduled task, sanitized. Scheduled tasks let the system stay current without anyone triggering it, overnight sourcing and prep, a morning brief, weekly reviews, periodic self-audits. They are orchestrators (top of the call stack), so unlike a department head they *can* dispatch specialists directly.

## What it does

Every weekday morning, before the operator is up:

1. Reads each department's status file, current state, blockers, next actions.
2. Dispatches a summarizer per department, in parallel.
3. Aggregates the summaries into one ranked brief: what changed overnight, what needs a decision today, what is blocked and on whom.
4. Surfaces reminders that are due and folds in anything left pending from prior briefs.
5. Renders the brief to a file the operator reads with their coffee, and archives the prior day's.

## Shape

```
schedule: weekdays 06:30 local
run:
    states   = read_all_department_status_files()
    summaries = parallel(summarize(dept) for dept in states)     # fan-out
    brief     = rank_and_merge(summaries, due_reminders(), pending_inserts())
    write(brief); archive(yesterday)
```

## Design notes

- **Single-writer.** Only this task writes the daily brief file, which prevents two processes racing to set the same state, the same single-source-of-truth discipline the dashboards use.
- **Read-only on source data.** It summarizes department state; it does not mutate it. Reporting and acting are kept separate.
- **Parallel fan-out.** Department summaries run concurrently, so wall-clock time is the slowest single summary, not the sum of all of them.
- **Human-in-the-loop.** The brief *surfaces* decisions for approval. It never actions them. A scheduled task can do a great deal of preparation overnight; it still wakes the operator up to a queue, not to a set of already-taken actions.
- **Resilient archiving.** If an upstream insert is never consumed, it accumulates rather than vanishing, a stale brief is recoverable; a lost one is not.
