# Executive Office: a multi-agent AI operations system

![Built with Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-d97757?style=flat-square)
![Departments](https://img.shields.io/badge/Departments-12-5aa2ff?style=flat-square)
![Agents](https://img.shields.io/badge/Agents-100%2B-34d399?style=flat-square)
![External actions](https://img.shields.io/badge/External_actions-human_approved-f5c451?style=flat-square)
![Approach](https://img.shields.io/badge/Applied_AI-orchestration-a78bfa?style=flat-square)

For 12+ years I have been the Chief of Staff and Strategy & Operations leader who builds the operating systems other organizations run on. Naturally, I built one for my own.

A personal, production multi-agent system I designed and run on Claude Code. It turns a large language model into a coordinated operating team of 100+ specialized agents that handle real day-to-day workflows: planning, research, drafting, pipeline management, reporting, and review.

I'm an operator, not an ML engineer. This is applied AI (orchestration, agent design, and workflow automation) built to be genuinely useful in daily work, with a human in the loop on anything that leaves the system.

![Executive Office Steering Deck](docs/steering-deck.png)

<sub>The Steering Deck: one glance across all 12 departments. Illustrative view captured at an earlier agent count; the live system renders from real state files locally and never commits private data, and the current counts are the ones stated throughout this README (12 departments, 100+ agents).</sub>

| | |
|---|---|
| **Departments** | 12, each a self-contained team with its own lead and specialists |
| **Agents** | 100+, each with one clear role, its own instructions, and a scoped tool set |
| **Flagship pipeline** | A 14-stage drafting → adversarial review → validation → go/no-go workflow |
| **External actions** | Zero autonomous ones; every send and submit waits for a human click |
| **Substrate** | Claude Code sub-agents, hooks, scheduled tasks, MCP integrations, slash commands, file-based memory |
| **Control surface** | 30+ slash commands; 20+ recurring scheduled jobs (overnight sourcing, briefs, self-audits) |
| **Operating scale** | Run daily over months: thousands of agent sessions, 150,000+ agent turns |

## Explore the system

| Document | What's inside |
|---|---|
| [ARCHITECTURE.md](./ARCHITECTURE.md) | The deep dive: orchestration and dispatch, the adversarial review pipeline, the human-in-the-loop gate model, state and memory, the QA critic layer, and model-tier routing. Six diagrams. |
| [docs/AGENT-CATALOG.md](./docs/AGENT-CATALOG.md) | The complete roster across 12 departments, leadership, and the QA team, each agent with its single job. |
| [docs/PIPELINE.md](./docs/PIPELINE.md) | The 14-stage work pipeline, stage by stage. |
| [docs/PATTERNS.md](./docs/PATTERNS.md) | Six engineering patterns worth stealing, with the failures that produced them. |
| [examples/](./examples) | Sanitized, runnable-shaped examples, including [a full pipeline run](./examples/pipeline-run-example.md) with a real truthfulness-gate kickback: an agent, a critic, a slash command, a hook, a scheduled task, a status file. |

## What it produces

This isn't a demo. It ships real, dated artifacts every day, all rendered locally from private state (nothing here is committed). A sampling of the output:

- **A daily executive brief**. A cross-department morning rollup: what each team did overnight, what needs a decision, what's due. One read to run the day.
- **Mission Control**. The dashboard above: every department's status, the pending-decision queue, and a live "what's left today" action hub. Regenerated on every change with hard invariant checks: every count must tie across every surface, or the build fails loud instead of shipping a wrong number.
- **Decision-ready work packages**. Each one drafted, adversarially reviewed, truthfulness-audited, humanized, and committee-approved through the 14-stage pipeline before it ever reaches me.
- **Living trackers**. Per-domain dashboards (pipeline, outreach, calendar, finance, training) that stay current because every agent writes its state after every action, and a shared completion layer so a thing marked done in one surface is done everywhere.
- **Drafts staged for one-click approval**. Outreach, replies, briefs, prep docs. The system prepares and surfaces; a human approves and sends. Nothing autonomous reaches the outside world.

## What it does
- Runs structured workflows across departments (research, communications, operations, planning, and more), each staffed by purpose-built agents with narrow, well-defined responsibilities.
- Coordinates multi-step pipelines where work fans out to specialists in parallel, then is verified and synthesized before it reaches me.
- Maintains living state (status files, dashboards, durable memory) so the system has continuity across sessions.
- Surfaces decisions to me for approval. It drafts and prepares, but never sends or submits anything externally on its own.

## Architecture

A top-level coordinator dispatches work to department teams; each department has a lead (planner and auditor) and a set of specialists. Only the top of the call stack orchestrates; leads plan and validate, they do not fan out work themselves. That one boundary is the backbone of the system.

```mermaid
flowchart TB
    Principal(("Human"))
    COS["Chief of Staff<br/>aggregation · daily brief · approval queue"]
    EA["Executive Assistant<br/>task list · day-of nudges"]
    Coach(["Strategic Coach<br/>system drift + capability review · advisory"])

    Principal --> COS
    Principal -.peer.-> EA
    Principal -.advisory.-> Coach

    COS --> D1["Careers"]
    COS --> D2["Calendar"]
    COS --> D3["Email"]
    COS --> D4["Communications"]
    COS --> D5["Lifestyle & Ops"]
    COS --> D6["Fitness"]
    COS --> D7["Research"]
    COS --> D8["Finance"]
    COS --> D9["Dashboard & Tools"]
    COS --> D10["Learning"]
    COS --> D11["Social & Marketing"]
    COS --> D12["Entrepreneur"]

    QA["Super-User QA: domain critics file tickets against every surface"]
    COS -.audited by.-> QA

    classDef p fill:#fde68a,stroke:#92400e,stroke-width:3px,color:#000
    classDef c fill:#bfdbfe,stroke:#1e40af,stroke-width:2px,color:#000
    classDef a fill:#fed7aa,stroke:#9a3412,stroke-dasharray:5 3,color:#000
    class Principal p
    class COS,EA c
    class Coach,QA a
```

- **Orchestration layer:** a top-level coordinator dispatches tasks to specialized sub-agents and aggregates their output into a single decision-ready result.
- **100+ specialized agents**, each with one clear role, its own instructions, and a scoped tool set.
- **Slash commands:** repeatable entry points for common multi-agent workflows.
- **Hooks:** automated checks that fire at defined points to enforce the system's rules.
- **Scheduled tasks:** recurring jobs that keep the system current without manual triggering.
- **External integrations (MCP):** connections to outside tools and data sources.
- **Rendered dashboards:** generated HTML views of system state for at-a-glance review.

## The flagship workflow

The highest-stakes pipeline in the system follows an **attack → defend → validate → decide** shape. Work is drafted, then handed to independent critics whose only job is to find what is wrong with it, then humanized, validated against a multi-gate checklist, and finally judged as a whole before anything reaches me.

```mermaid
flowchart LR
    In[Input] --> Strat["Strategy<br/>positioning"]
    Strat --> Draft["Drafting specialists<br/>(parallel)"]
    Draft --> Attack{"Adversarial review"}
    Attack --> A1["Coverage audit"]
    Attack --> A2["Truthfulness audit<br/>no fabrication"]
    Attack --> A3["Skeptic simulation<br/>first-impression read"]
    Attack --> A4["Red-team critic<br/>worst-case interpretation"]
    A1 & A2 & A3 & A4 --> Hum["Humanization editor"]
    Hum --> QC["Multi-gate QC"]
    QC --> Comm{"Committee<br/>go / no-go"}
    Comm -->|go| Q["Human review queue"]
    Comm -->|kickback| Strat
    Q --> Person(("Human approves"))

    classDef person fill:#fde68a,stroke:#92400e,stroke-width:2px,color:#000
    class Person person
```

The agent that **writes** is never the agent that **grades**. Optimism and skepticism are separated into different agents on purpose. And the system that drafts an external message is structurally incapable of sending it.

## Design principles
- **Human in the loop.** The system drafts and prepares; a person approves and sends. No autonomous external actions.
- **Quality gates.** Independent drafting, adversarial review, and validation run before any output is considered done.
- **Single source of truth.** Invariant checks prevent state drift across the system's many files.
- **Honesty by construction.** Verification agents check every claim against ground-truth source material.

## Engineering decisions worth stealing

These generalize well beyond my own use of them.

- **Planners are not orchestrators.** Sub-agents can't spawn sub-agents. A department lead plans and audits, then returns a structured instruction for the top-level context to execute. Conflating "manager" with "dispatcher" produces silent no-ops; making the boundary explicit fixed an entire class of failures.
- **Status freshness as a protocol.** Every department writes a status file after every meaningful action, and all dashboards render from those files. A stale file is a stale dashboard, so freshness is a rule, not a nicety.
- **Render-time invariants that fail loud.** Dashboards are regenerated by a deterministic pipeline that runs audits on every build: every count must agree across every surface, and every clickable element must be wired, or the build fails instead of shipping wrong numbers.
- **Human-confirmed state is immutable to automation.** When a person marks something done, no background job may silently revert it. The reconciler can heal missing data but is structurally incapable of demoting a human's confirmed action.
- **Determinism where it counts.** Creative judgment is model-driven; counting, joining, rendering, and auditing are plain code. A language model is a poor database.

## Stack
Claude Code (sub-agents, slash commands, hooks, scheduled tasks, MCP integrations), Python (state rendering and audits), Markdown and JSON for state and memory.

See [`examples/`](./examples) for sanitized agent and workflow definitions, and [ARCHITECTURE.md](./ARCHITECTURE.md) for a deeper look at the design.

## A note on scope
This repository is an architecture and patterns showcase. The running system operates on private data that lives locally and is never committed. What's here is the design, not the data.

---
Built and maintained by Kyle Littlejohn. Applied-AI orchestration and workflow automation, not model training or ML engineering.
