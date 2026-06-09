# Executive Office — a multi-agent AI operations system

A personal, production multi-agent system I designed and run on Claude Code. It turns a large language model into a coordinated operating team of 60+ specialized agents that handle real day-to-day workflows: planning, research, drafting, pipeline management, reporting, and review.

I am an operator, not an ML engineer. This is applied AI — orchestration, agent design, and workflow automation — built to be genuinely useful in daily work, with a human in the loop on anything that leaves the system.

## What it does
- Runs structured workflows across departments (research, communications, operations, planning, and more), each staffed by purpose-built agents with narrow, well-defined responsibilities.
- Coordinates multi-step pipelines where work fans out to specialists in parallel, then is verified and synthesized before it reaches me.
- Maintains living state (status files, dashboards, durable memory) so the system has continuity across sessions.
- Surfaces decisions to me for approval. It drafts and prepares, but never sends or submits anything externally on its own.

## Architecture
- Orchestration layer: a top-level coordinator dispatches tasks to specialized sub-agents and aggregates their output into a single decision-ready result.
- 60+ specialized agents, each with one clear role, its own instructions, and a scoped tool set.
- Slash commands: repeatable entry points for common multi-agent workflows.
- Hooks: automated checks that fire at defined points to enforce the system's rules.
- Scheduled tasks: recurring jobs that keep the system current without manual triggering.
- External integrations (MCP): connections to outside tools and data sources.
- Rendered dashboards: generated HTML views of system state for at-a-glance review.

## Design principles
- Human in the loop. The system drafts and prepares; a person approves and sends. No autonomous external actions.
- Quality gates. Independent drafting, adversarial review, and validation run before any output is considered done.
- Single source of truth. Invariant checks prevent state drift across the system's many files.
- Honesty by construction. Verification agents check every claim against ground-truth source material.

## Stack
Claude Code (sub-agents, slash commands, hooks, scheduled tasks, MCP integrations), Python (state rendering and audits), Markdown and JSON for state and memory.

---
Built and maintained by Kyle Littlejohn. Applied-AI orchestration and workflow automation — not model training or ML engineering.
