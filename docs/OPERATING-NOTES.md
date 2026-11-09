# Operating notes

How I think about running this system, and what it has taught me. This is my experience with one system, not a set of universal rules. The architecture is in [ARCHITECTURE.md](../ARCHITECTURE.md); the claims and their evidence are in [EVIDENCE.md](./EVIDENCE.md).

## The problem I was solving

In my own work, the bottleneck was coordination, not effort. The hard part was deciding which of twenty open threads gets attention next, which number is actually true right now, and which draft is ready to leave.

A faster draft does not change who is accountable for the decision that follows it. A draft that lands in an inbox nobody is watching is another open thread. So I wanted a system that carries the coordination load and still puts every consequential decision in front of a person. In my case that is an operating-model question as much as a tooling question.

## Operating philosophy

Four principles I rely on across the departments.

- **Attention is the scarce resource.** The system exists to keep one queue short and honest: what I look at next. Drafting, research, reconciliation and tracking serve that queue.
- **Outcomes over system size.** A smaller system that produces real movement beats a larger one that produces internal activity. Agent counts and dashboards are not the point. Decisions made and work shipped are.
- **One queue per decision.** Each type of decision (approve, send, submit, review) surfaces in one place, rendered from one source of state. Two queues for one decision is how things get missed or done twice.
- **A human on every decision that leaves the system.** The system drafts and prepares freely. It does not act on the outside world without a person choosing to. This is built as layers (an instruction, a runtime check and a decision surface). The [hook example](../examples/hook-example.md) explains the difference between them and what is not shown publicly.

## Governance habits

- **Gates.** Nothing external ships without my click. The highest-stakes workflow follows a draft, attack, validate, decide shape: independent critics look for problems, a QC step checks the files, and a committee agent makes a final call. The agent that writes a piece of work is not the agent that grades it.
- **Receipts.** Meaningful actions leave a record: a status file, a ledger entry, a dated artifact. Claims about what happened are checked against a record before they are published.
- **Same-turn rule capture.** When I set a new standing rule, it gets written down in the same working session, and where it can be checked mechanically it becomes a check in code.
- **Self-audit.** Critics review the system's own output on a schedule, and domain critics file tickets against each surface.

## Lessons from the operating record

Three incidents from my private operating record. They are my account of events that cannot be inspected here.

**Measurement caught a wrong number before it drove a decision.** A cadence figure in the career pipeline looked like a collapse, and a response was being planned around it. The system's own weekly data contradicted it. The figure had come from a stale copy of a log and a wrong week boundary. I had the correction logged the same night and the data path repaired so the figures could not diverge again. The lesson I took: a measurement layer earns trust by catching wrong numbers and recording the correction openly.

**A split in the source of truth cost work before I found it.** An operational log had split into two paths without anyone deciding that. Fourteen legitimate records sat in the path nobody read. A reminder to check both paths would have been the weak fix. I had the secondary path replaced with a symlink to the primary, so there is one file. The lesson: when a process failure is really a structure failure, fix the structure.

**A scoring model was checked against past outcomes before I used it.** Before a new priority-scoring model went live, I had it run back against my own historical record of interview outcomes and rejections. It separated the two groups, and the one low-scoring exception was a case with thin data. **Limits:** this was a historical comparison on my own records. The sample size, the design, the leakage controls and the evaluation method are not published here, so it does not establish that the model will predict future outcomes. I treat it as a sanity check, not as validation.
