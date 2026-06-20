# Engineering patterns

Patterns this system arrived at, usually by getting them wrong first. They generalize well beyond a job search, to any agent system that has to be correct, durable, and trustworthy rather than just demo-able.

## 1 · Planners are not orchestrators

Sub-agents cannot spawn sub-agents. The runtime strips the dispatch tool from any agent spawned as a sub-agent, regardless of what its config claims. Only the top of the call stack (a human session, a slash-command handler, or a scheduled task) can fan work out.

The failure this prevents is subtle and silent: a "manager" agent appears to dispatch its team, the prompt reads as if the calls fired, and nothing happens. The fix is to make the boundary explicit in the architecture itself. A department head *plans and audits* and returns a structured instruction; the orchestrator at the top of the stack *executes* the fan-out. When something is broken, you know which layer to look at because the layers are real, not implied.

**The lesson:** know exactly which layer of your stack is allowed to act, and don't let a convincing prompt fool you into thinking a lower layer can.

## 2 · Status freshness as a protocol

Every department writes a `status.json` after every meaningful action: headline, metrics, recent activity, blockers, next step. Every dashboard renders *from* those files; none holds its own copy of the truth. There is one source for every number.

Updating the file is the last step of every workflow, enforced as a rule rather than left to discipline. A stale file is a stale dashboard is a moment where the operator stops trusting the system, and trust, once lost, is expensive to rebuild. So freshness is treated as part of the work, not cleanup after it.

## 3 · Render-time invariants that fail loud

Dashboards are not hand-edited HTML. A deterministic pipeline regenerates them from the status files and tracking data, and on every build it runs audits:

- a **number-tie** audit: every count must agree across every surface, or the build fails;
- an **interactivity** audit: every element that looks clickable must be wired to a real handler, or the build fails;
- **domain invariants**: house rules like "an item reaches the ready queue only if it passed both validation and committee," asserted at render time.

The point is that wrong numbers should crash the build, not ship quietly. A dashboard that confidently displays a number nobody can reconcile is worse than no dashboard.

## 4 · Human-confirmed state is immutable to automation

When a person marks something done, no background job may silently undo it.

This one was learned the hard way. An automated reconciler, unable to tell a human's confirmation from its own stale write, kept reverting confirmed records to an earlier state. The fix is a write-guard with an asymmetric contract: it *may* heal a record (backfill missing provenance on something the human clearly did) but it *may not* demote a human-confirmed record to a lower state, ever. The revert path was deleted entirely, because once the system can no longer create a false confirmation at write time, that path can only eat real ones.

**The lesson:** when in doubt, automation trusts the human's signal. Losing a real confirmation costs far more than keeping a rare stray one.

## 5 · Determinism where it counts

Creative judgment is model-driven. Counting, joining, rendering, auditing, and enforcing invariants are plain code.

A language model is a poor database and a worse calculator. Asking one to tally a column or guarantee an invariant is asking for confident, occasional wrongness. So the system draws a hard line: agents decide *what* the résumé should say or *whether* a venture is worth pursuing; deterministic scripts decide *how many* roles are in the queue and *whether* every surface agrees. The reliability of the whole system rests on keeping that line clean.

## 6 · Defense in depth on the one rule that matters

No external action (submit, send, write to a calendar) happens without an explicit human action, and that rule is enforced at three independent layers so a single missed check can't leak it: every agent's prompt forbids it, a runtime hook intercepts the tool call, and the interface only ever presents a queue for human approval. Internal mechanics flow freely; the gate exists solely for anything the outside world would see.

---

The throughline: build for the case where it has to be *right*, not just impressive in a demo. Separation of concerns, invariants that fail loud, and a human on every decision that matters are what make an agent system you can actually rely on day to day.
