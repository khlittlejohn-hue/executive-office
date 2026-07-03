# Status file: the freshness protocol

An example of the contract every department implements, sanitized. Each department writes one status file after every meaningful action, and every dashboard renders from these files. A stale file is a stale dashboard, so freshness is enforced as a rule.

## The file

```json
{
  "department": "research",
  "lastUpdated": "2026-01-15T14:32:00Z",
  "headline": "3 briefs in flight · 1 awaiting review · 0 blocked",
  "metrics": {
    "inFlight": 3,
    "awaitingReview": 1,
    "completedThisWeek": 7
  },
  "blockers": [],
  "next": "Synthesize the two market briefs into a single recommendation.",
  "recentActivity": [
    { "ts": "2026-01-15T14:32:00Z", "summary": "Completed competitor analysis; handed to brief writer." },
    { "ts": "2026-01-15T11:10:00Z", "summary": "Opened deep-dive on supplier landscape." }
  ]
}
```

## Why it works this way

- **Single writer per file.** Only the owning department writes its status file, which prevents two agents racing to set the same field.
- **Render, don't duplicate.** Dashboards never hold their own copy of the truth; they read these files at build time. There is one source for every number.
- **Freshness is the contract.** Updating the file is the last step of every workflow, not an afterthought. If the work happened, the file moved.
- **Machine- and human-readable.** The same file drives the rendered dashboard and can be read directly when debugging.

## The invariant

At render time, the totals in every status file must reconcile with the underlying tracking data. If a department claims three briefs in flight but the tracker shows two, the build fails loudly rather than shipping a dashboard that quietly lies.
