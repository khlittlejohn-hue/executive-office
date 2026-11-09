# Claim-to-evidence inventory

This page lists the main claims made in this repository and says what kind of evidence supports each one. It exists so a reader can tell what can be inspected here from what rests on my own account of a private system.

## Evidence levels

| Level | Meaning |
|---|---|
| **A. Described** | Documented design or architecture. The text says it; nothing here executes it. |
| **B. Public configuration or code** | The relevant files are in this repository and can be read. |
| **C. Public demonstration** | A runnable example with tests in this repository. It shows the pattern on synthetic data, not the private system. |
| **D. Recorded evaluation** | A measurement was made and recorded. State the sample and method, or say they are not published. |
| **E. Private operational claim** | Something I observed in the private system. It cannot be independently inspected from this repository. |

## Inventory

| Claim | Level | Where | Limits |
|---|---|---|---|
| The system has 14 departments and 120+ named agents (123 listed in the catalog) | A | [docs/AGENT-CATALOG.md](./AGENT-CATALOG.md) | A catalog count shows what is described. It does not show that every agent is deployed, invoked, tested or effective. The arithmetic does reconcile (see below). |
| Anything the outside world would see waits for a human decision | A, C, E | [ARCHITECTURE.md](../ARCHITECTURE.md), [hook example](../examples/hook-example.md), [demo/approval.py](../demo/approval.py) | The hook example is pseudocode. The demo shows a blocked action, an approval tied to the exact action, single use and expiry on synthetic data. It does not show the private hook, tool coverage or how the approval record is protected. The demo binds an approval to the exact arguments; I do not claim the private hook does. |
| A truthfulness check rejects a claim that would not survive an interview question | A | [pipeline example](../examples/pipeline-run-example.md), [PIPELINE.md](./PIPELINE.md) | The example is a synthetic illustration. No rejection rate or sample of real rejections is published. |
| The agent that writes is not the agent that grades | A | [ARCHITECTURE.md](../ARCHITECTURE.md) | This is a role design. It is held by instructions and review, not by removing every ability to edit. |
| One writer produces the daily brief, whether it is run on demand or on a schedule | A, E | [slash command](../examples/slash-command-example.md), [scheduled task](../examples/scheduled-task-example.md) | The writer is the Chief of Staff agent in brief mode. There is no file lock, so single ownership is a convention. |
| Dashboards refuse to render when counts disagree | C, E | [demo/brief.py](../demo/brief.py) | The demo shows a rollup refused when it disagrees with its sources. The private dashboards are not published. |
| In my configuration, sub-agents are not given the dispatch tool, so only the top of the call stack dispatches | A | [docs/PATTERNS.md](./PATTERNS.md) | Observed in my configuration. Anthropic's documentation describes sub-agent nesting as configurable, so this is a design choice I rely on, not a platform guarantee. |
| A historical back-test of a scoring model separated interviews from rejections | E, D (partial) | [OPERATING-NOTES.md](./OPERATING-NOTES.md) | It used my own pipeline records. The sample, method and leakage controls are not published, so it is not evidence that the model predicts future outcomes. |
| A wrong cadence figure was caught by the measurement layer and corrected | E | [OPERATING-NOTES.md](./OPERATING-NOTES.md) | My account of a private incident. |
| A split log path was found and replaced with a symlink | E | [OPERATING-NOTES.md](./OPERATING-NOTES.md) | My account of a private incident. |
| The system produces a daily brief and other dated artifacts | E | [README](../README.md) | Private. The Steering Deck screenshot is synthetic. |
| 48 slash commands, 98 scheduled-task definitions (19 marked retired or disabled), 307 saved sessions | E | [README](../README.md) | Counted on 2026-11-09 on my machine. These are counts of what exists, not measures of use or value. |

## Catalog arithmetic

The catalog states these figures, and they reconcile:

- Department specialists: Careers 23, Research 3, Finance 10, Calendar 3, Email 4, Communications 6, Lifestyle and Operations 7, Fitness 7, Dashboard and Tools 6, Learning 6, Social and Marketing 6, Entrepreneur 6, App Development 13, KLJ Ventures 3 = **103**.
- 103 specialists + 3 leadership roles + 3 model-routing agents + 14 QA agents = **123**.
- 123 + 3 apex governance agents = **126**.

Two notes on how the arithmetic was checked. The section headings in the catalog sum to 120 (103 department specialists, 3 model-routing agents, 14 QA agents), and the 3 leadership roles bring that to 123. App Development's 13 is one portfolio manager plus four roles for each of three products. The 3 apex governance agents are counted in the totals paragraph but are not listed individually in the catalog, so the figure of 126 rests on that paragraph, and 123 is the number of agents the catalog itself lists.

## Possible additions

- A sanitized public version of the approval hook, so approval handling, expiry and tool coverage can be read directly.
- Inventory counts generated by a committed script, so they are reproducible.
