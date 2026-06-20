# Architecture

A deeper look at how the Executive Office is structured. Sanitized companion to the [README](./README.md).

## The shape

```
Human (principal)
├── Chief of Staff ............ cross-department aggregation, daily brief, approval queue, dispatch routing
├── Executive Assistant ....... hour-by-hour task list, day-of nudges, quick lookups (peer to CoS)
├── Strategic Coach ........... advisory; reviews the whole system for drift and unused capability
├── Super-User QA ............. domain critics + a QA program manager file and route tickets
└── 12 Departments
    └── each: one lead + N specialists
```

The human is the only actor who performs irreversible external actions. Everything below drafts, prepares, validates, and surfaces.

## Departments

Each exposes the same contract: a status file (current state, metrics, recent activity, blockers) that the dashboards render from, and a lead that owns it.

| Department | Scope |
|---|---|
| Careers | A job-search pipeline end to end |
| Calendar | Scheduling, conflict resolution, meeting prep |
| Email | Inbox triage, draft replies, escalations |
| Communications | Voice and tone for all external writing |
| Lifestyle & Ops | Bills, travel, subscriptions, events |
| Fitness | Training plans, analytics, nutrition |
| Research | Deep-dive analysis on companies, people, decisions |
| Finance | Capital allocation, investment research, tax posture |
| Dashboard & Tools | The internal tooling and rendering pipeline |
| Learning | Curating and adopting workflow improvements |
| Social & Marketing | Content pipeline and cadence |
| Entrepreneur | Venture evaluation |

## The orchestration rule

> Sub-agents cannot spawn sub-agents.

This is the load-bearing constraint. Only the top of the call stack (a human session, a slash-command handler, or a scheduled-task runner) can fan work out to specialists. A department lead is a planner and auditor: it decides what should happen and validates what did, but it returns a structured instruction for the orchestrator to execute rather than executing the fan-out itself. Getting this wrong produces silent no-ops, where a "manager" agent appears to dispatch its team but the calls never fire.

## The approval gate (defense in depth)

No external action happens without an explicit human action, enforced at three layers so a single missed check can't leak:

1. **Per-agent instruction**. Every agent's prompt forbids outbound actions.
2. **Runtime hook**. A pre-tool-use hook intercepts tool calls and blocks external side effects unless a per-action approval flag is present.
3. **Surface-level UX**. The dashboards present a queue; the human approves items one at a time.

Internal mechanics (editing files, writing dashboards, drafting documents) flow freely under a standing authority. The gate is specifically about anything the outside world would see.

## The rendering pipeline

Dashboards are not hand-edited HTML. A deterministic renderer ingests every department's status file plus tracking data and emits the HTML surfaces. On every build it runs:

- A **number-tie audit**: every count must agree across every surface, or the build fails.
- An **interactivity audit**: every element that looks clickable must be wired, or the build fails.
- **Invariant checks**: domain rules (for example, "an item reaches the ready queue only if it passed both validation and committee") asserted at render time.

Creative judgment is model-driven; counting, joining, and asserting are plain code.

## Human-confirmed state is immutable to automation

A recurring background job once flipped human-confirmed records back to an earlier state because it couldn't tell them from its own stale writes. The fix is a write-guard with an asymmetric contract: it may heal a record (backfill missing provenance on something the human clearly did), but it may not demote a human-confirmed record to a lower state, ever. When in doubt, the guard trusts the human's signal: losing a real confirmation costs more than keeping a rare stray one.

## Memory

Durable facts live as one-fact-per-file markdown with a loaded index, read at the start of every session: who the principal is and how they work, corrections and confirmed approaches with the reasoning behind them, ongoing constraints, and pointers to external resources. A correction made once becomes a standing rule instead of being re-litigated every session.

---
Sanitized for public showcase. The live system runs locally against private data.
