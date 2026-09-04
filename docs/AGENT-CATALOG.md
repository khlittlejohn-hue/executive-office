# The agent catalog

The full function-first index of the system: every layer, every department, and the single job each agent holds.

The design rule is one agent, one job. Each agent has its own system prompt, its own scoped tool set, and a name that states its function. A single-purpose agent named for its job is a unit you can hold in your head. It is far easier to reason about, trust, and debug than `agent_07`, because its name tells you what it does and its scope tells you what it will not do.

Three principles fall out of that rule and recur across every table below.

The agent that **writes** is never the agent that **grades**. Optimism and skepticism live in different agents on purpose, so a draft meets a genuinely independent critic rather than its own author grading its own homework.

Planners are not orchestrators. A department head plans and audits, then returns a structured instruction for the top-level context to run. Leads do not fan out work themselves. That one boundary is the backbone of the system.

Nothing autonomous reaches the outside world. Every agent below drafts and prepares. A human approves and sends. The functions describe what each agent produces, not what it dispatches.

Each row pairs a function with the role that owns it.

## Contents

- [Leadership layer](#leadership-layer)
- [Model-tier routing team (3)](#model-tier-routing-team-3)
- [Careers: the job-search pipeline (23)](#careers-the-job-search-pipeline-23)
  - [The case-study studio (8)](#the-case-study-studio-8)
- [Research and Intelligence (3)](#research-and-intelligence-3)
- [Finance (10)](#finance-10)
- [Calendar and Scheduling (3)](#calendar-and-scheduling-3)
- [Email Operations (4)](#email-operations-4)
- [Communications (6)](#communications-6)
- [Lifestyle and Operations (7)](#lifestyle-and-operations-7)
- [Fitness and Performance (7)](#fitness-and-performance-7)
- [Dashboard and Tools (6)](#dashboard-and-tools-6)
- [Learning and Improvement (6)](#learning-and-improvement-6)
- [Social and Marketing (6)](#social-and-marketing-6)
- [Entrepreneur and Ventures (6)](#entrepreneur-and-ventures-6)
- [Super-User QA: the standing critics (14)](#super-user-qa-the-standing-critics-14)
- [Totals](#totals)

## The count, verified

87 department specialists, plus the 3-role leadership layer, the 3-agent model-tier routing team, and the 14-agent QA team, is 107 named agents. Add the 3-agent apex governance layer and the total is 110, which is why the system is described by the round floor of 100+. The full breakdown, department by department, is in [Totals](#totals) at the bottom.

## Leadership layer

The three roles that sit above and beside the departments. The Chief of Staff aggregates and reports; the Executive Assistant runs the day; the Coach reviews the whole system from outside it.

| Function | Role |
|---|---|
| Cross-department aggregation, daily brief, approval queue, dispatch routing. The single point of accountability. | Chief of Staff |
| Hour-by-hour task list, day-of nudges, quick lookups, inbound routing. Peer to the CoS, not under it. | Executive Assistant |
| Sits outside every pipeline. Reviews all agents for drift and contradiction, watches sessions for repeated friction, scans for unused platform capability. Proposes edits, never applies them. | Strategic Coach |

## Model-tier routing team (3)

Not every task deserves the same model. Three agents hold the routing judgment itself, which tier a task deserves, and the final call when work escalates all the way up. (See [ARCHITECTURE.md § Model-tier routing](../ARCHITECTURE.md#6--model-tier-routing) for the cheap/mid/strong pattern this team runs.)

| Function | Role |
|---|---|
| Runs the default execution tier (standard drafting, research, structured pipeline work, first-pass everything); escalates upward only when a task specifically calls for it. | Sonnet-tier Operator |
| Takes on complex builds, hard debugging, and adversarial review; escalates judgment calls upward, de-escalates mechanical work downward. | Opus-tier Specialist |
| Holds final say on the highest-reasoning-tier work; routes work down to the other two and signs off before anything ships. | Fable-tier Lead |

## Careers: the job-search pipeline (23)

The flagship department. A positioning brief opens the pipeline; parallel drafting fans out; independent critics attack the package; a committee makes the final go or no-go call. Drafts only. A human submits every application.

| Function | Role |
|---|---|
| Plans and audits the pipeline; owns the prepped queue; never dispatches, because planners are not orchestrators. | Department Head |
| Bookends the pipeline: sets the positioning brief first, makes the final holistic go or no-go last. | Strategy Lead and Committee Chair |
| Mirrors the job description's language where truthful; preserves a locked canonical format. | Resume Tailor |
| Independently scores keyword coverage against the job description; kicks back to the writer below threshold. The auditor is never the author. | ATS Auditor |
| Cover letters, cold outreach, InMails, connection notes, referral asks. Three voice registers. Drafts only. | Cover-Letter and Outreach Writer |
| Finds named recruiters, hiring managers, and warm paths; reads company priorities and what the company actually values. | People and Company Intel |
| The truthfulness gate. Flags fabrication, inflated metrics, and borrowed pedigree across resume, cover letter, and outreach. Nothing ships without sign-off. | Achievement Verifier |
| Reads the package the way a skeptical recruiter does in 15 seconds, hunting for reasons to reject. | Recruiter Simulator |
| Argues the worst-case interpretation: logical gaps, contradictions, interview trap-doors. | Red-Team Critic |
| Rewrites so the output reads like a person wrote it: varied rhythm, broken parallelism, no machine tells. | Humanization Editor |
| A multi-gate validation pass over structure, ATS, format adherence, and voice before the committee sees it. | QC Reviewer |
| The single writer for status flips; records applied dates, files, and provenance with hard validation. | Dashboard Keeper |
| Scores aging applications and outreach, drafts personalized nudges on a one- and two-week cadence. | Follow-up Tracker |
| Cross-references the resume against likely questions, builds STAR stories, predicts skepticism, drafts questions to ask back. | Interview Prep |
| Reads the professional feed for hiring posts and warm paths the job boards never surface; classifies and fit-scores. Surfaces only. | Feed Scout |

### The case-study studio (8)

A cell inside Careers, added 2026-07-11, that activates for take-home and live case-study interviews. Owns the narrative and the deliverable end-to-end, running its own internal fan-out-then-critique pass before anything reaches the candidate.

| Function | Role |
|---|---|
| Owns the narrative and the deliverable end-to-end: decodes the prompt, sets the day-1 hypothesis, orchestrates the studio, holds the final go gate on the artifact. | Studio Lead |
| Deep-dives the case company: business model, strategy, competitors, leadership, the real problem behind the prompt's wording. | Account Research |
| Grounds every recommendation in a real precedent or industry benchmark so it reads as proven, not invented. | Precedent and Benchmarks |
| Owns the quantitative backbone: market sizing, unit economics, the financial model, sensitivity analysis. | Numbers and Rigor |
| Turns the studio's intel into the answer-first slide deck and executive summary; owns structure, flow, and copy. | Deck Architect |
| Applies the target company's visual identity so the deliverable looks board-grade, not generic. | Packaging and Brand |
| Teaches case methodology and frameworks, then runs mock presentations and hostile Q&A so the candidate can defend it live. | Methodology Coach and Rehearsal |
| Role-plays the actual interviewers, attacking every claim and surfacing the hard questions before the real thing. | Adversarial Interviewer Simulator |

## Research and Intelligence (3)

Deep-dive analysis on companies, people, products, and decisions. Rigor first, then readability, then the zoom-out frame when it is load-bearing.

| Function | Role |
|---|---|
| Deep-dive analyst on companies, people, and decisions. Reads everything, cites sources, never accepts a vague answer. | Department Head |
| Turns dense analysis into a clear executive one-pager. Where the head is rigor, this is readability. | One-Pager Writer |
| Adds the zoom-out frame of history, power, and the long game when "why now" is load-bearing. | Macro Context |

## Finance (10)

Two desks under one head: a strategy-and-operations desk that drafts the mechanics, and an investment-research desk that debates before it concludes. Every external action queues for approval. Drafts; never files; never executes.

| Function | Role |
|---|---|
| Capital allocation, investment philosophy, risk posture, the strategy call. Coordinates both desks. | Department Head |
| Monthly P&L, category spend, budget tracking, runway math. Cites numbers, never invents them. | Bookkeeping and Cash Flow |
| Tax-loss harvesting, retirement-account architecture, capital-gains posture. Drafts; never files; recommends a licensed CPA at the line. | Tax Strategy |
| Investing from zero: accounts, funding mechanics, first trades explained at exactly the right level. | Education Coach |
| Allocation, rebalancing plans, trade tickets. Drafts the mechanics; never executes. | Portfolio Operations |
| Leads the investment desk, synthesizes desk views, writes the lead thesis memos. Cites sources; the principal decides. | Head of Research |
| Macro, rates, and the Fed regime translated into market implications. | Macro Analyst |
| Tech, growth, and disruption read with an operator's instinct, not a sell-side one. | Growth Analyst |
| Quality, fundamentals, and defensives: balance sheets, moats, capital-allocation discipline. | Quality Analyst |
| The bear case on every position. Reads the downgrade thesis and the sector headwind. The most important critic on the desk. | Contrarian and Red-Team |

## Calendar and Scheduling (3)

Owns the week. Reviews the next seven days, resolves conflicts, protects focus blocks, and primes every meeting with context. All schedule changes require approval.

| Function | Role |
|---|---|
| Reviews the next seven days, resolves conflicts, enforces no-meeting rules, drafts reschedule proposals. | Department Head |
| Prepares briefing packets for upcoming meetings: location, attendees, prep needed, what was last said. | Day-of Logistics |
| Pulls cross-meeting context so the principal walks in primed: last conversation, open threads, recent posts. | Cross-Meeting Research |

## Email Operations (4)

Reads the inbox, categorizes against fixed buckets, decides priority versus noise, and drafts every reply into a queue. Nothing sends; drafts land ready for a human to send.

| Function | Role |
|---|---|
| Reads the inbox, categorizes against the buckets, escalates priority items, routes the rest to the team. | Department Head |
| The bulk volume work: labels, archives obvious noise, marks low-priority newsletters and alerts. | Triage Worker |
| Drafts careful, articulate replies to recruiters, hiring managers, and executive contacts. Drafts land as drafts. | Formal Drafter |
| Handles the tricky threads: declines, ghosted follow-ups, awkward reschedules, without escalating them further. | Escalation Handler |

## Communications (6)

Voice and tone for all external writing that is not the job search: thank-yous, relationship correspondence, networking, public posts. The department head holds a veto on anything that does not sound like a person. Drafts only.

| Function | Role |
|---|---|
| Owns voice and tone for all non-Careers external writing; holds veto on anything off-voice. | Department Head |
| Thank-you notes, LinkedIn posts, thought-leadership. Sharp voice, no fluff, a bias for the concrete. | Personal Writing |
| Long-arc warm contacts: old colleagues, mentors, referrers. The keep-the-door-open register, tracked per person. | Relationship Correspondence |
| Cold-warm intros and anything where wit matters more than brevity, with a real point underneath. | Networking Charm |
| Reads every outbound draft for diction and voice match; owns the living voice spec and the corrections ledger. Advisory, never blocks. | Voice and Vibes Check |
| The binding final voice gate: reads every outbound draft the way the principal would the moment before sending, and rules on one question, does this sound like a person and is it free of every machine tell. Blocks; never sends. | Final Voice Gate |

## Lifestyle and Operations (7)

Life logistics and the fun side of life: bills, subscriptions, travel, documents, provisions, plus events and nightlife, plus the file system that everything else depends on. External actions queue for approval.

| Function | Role |
|---|---|
| Runs the life-logistics tracker end to end and coordinates the team. | Department Head |
| Reminders and recurring obligations: appointments, deadlines, home admin, on-sale windows. | Reminders |
| Travel and documents: flights, hotels, transfers, passport and renewal windows, packing. | Travel and Documents |
| Shopping, provisions, and subscriptions: what renews when, what to cancel, gift reminders. | Provisions |
| Bills, disputes, and paperwork: fee reviews, cancellation drafts, transaction watch. Drafts; routes formal sends through Email. | Bills and Disputes |
| Nightlife, festivals, and events: watches on-sale windows, drafts ticket briefs. Never buys; surfaces only. | Events and Nightlife |
| File-system steward: naming conventions, status-based filing, tidy sweeps. Archives, never hard-deletes; never breaks a path a pipeline depends on. | File Steward |

## Fitness and Performance (7)

Owns the training calendar and the season plan. Analytics, hard workouts, and fundamentals as separate voices, plus nutrition, the race calendar, and advisory health tracking. Race registrations queue for approval.

| Function | Role |
|---|---|
| Owns the training calendar and season plan; coordinates the team. | Department Head |
| Reads load data, recovery markers, and trend lines; flags overtraining. Analyzes workouts, does not design them. | Training Analytics |
| Designs threshold sessions, race-pace runs, and peak-week workouts; sets race-day pacing. | Hard Workouts |
| The necessary work: drills, technique, form, warmups, mobility. Grace before power. | Fundamentals |
| Nutrition tracking and the recipe library; translates fitness tips into fueling guidance. Surfaces grocery lists; never buys. | Nutrition |
| The race calendar and registration windows: majors, circuits, qualifiers. Never misses a window. | Race Calendar |
| Advisory-only health tracking: symptom logs, questions for doctor visits, longitudinal patterns. Never prescriptive; never a substitute for care. | Health Tracking |

## Dashboard and Tools (6)

The internal tooling team that builds the surfaces everyone else renders to, plus the public-facing web presence. UI direction, frontend, the render pipeline, a bold counterweight, and a public-web engineer who never auto-pushes.

| Function | Role |
|---|---|
| Owns the internal-tools queue; scopes requests, dispatches, pushes back when ideas do not pencil out. | Department Head |
| UI and UX direction; owns the steering dashboard end to end and the canonical style guide. | UI/UX Director |
| Frontend implementation: HTML, CSS, JS, visual polish, the "looks tight" pass. | Frontend Engineer |
| Backend and systems: the render pipeline, the data ingestion, the Python infrastructure. | Backend Engineer |
| The bold counterweight: pushes for stronger visuals, better naming, bigger ambition against competent-but-boring. | Ambition Pusher |
| The public website and public repositories: cleanup, polish, shipped enhancements. Builds and previews locally; never auto-pushes. | Public Web Engineer |

## Learning and Improvement (6)

Curates, adopts, and measures workflow improvements over time. Categorizes an incoming tip, verifies it, turns it into a clean table, implements the adopted ones within the approval rules, and tracks what actually sticks.

| Function | Role |
|---|---|
| Owns the tip-curation pipeline end to end; wraps extractions and verdicts into an adoption workflow. | Department Head |
| First-pass categorizer and router: classifies each shared link, extracts structured data, routes to the right destination. | Categorizer and Router |
| Owns the canonical tips table the principal reads and edits; turns raw verdicts into a coherent view. | Tip Curator |
| Executes an adopted tip precisely within the approval rules; writes the change record. No improv, no scope creep. | Implementer |
| The longitudinal library: reads adopted and skipped records over time and surfaces the patterns. | Pattern Analyst |
| Owns the tips dashboard: the clean visual view, rendered from the tracker. | Dashboard UI |

## Social and Marketing (6)

The content pipeline: ideas, production, brand voice, cadence, and the commercial layer. Drafts and ships plans; a human records and posts every piece.

| Function | Role |
|---|---|
| Owns the content roadmap, the video pipeline, and posting cadence; scopes requests and dispatches. | Department Head |
| Content ideas and hook angles; owns the idea backlog and finds the unexpected angle. | Ideas and Hooks |
| Production and editing: the full script, b-roll cues, captions, hashtags, posting specs. | Production |
| Brand voice and on-camera coaching: what sounds like the principal and what does not; the on-brand gut check. | Brand Voice |
| Posting cadence and audience tracking: the content calendar, post-publish metrics, what is hitting and why. | Cadence and Audience |
| The commercial layer: the monetization roadmap, sponsorship and pricing strategy, revenue implications. | Monetization |

## Entrepreneur and Ventures (6)

A panel that pressure-tests every new venture from 5 angles, then synthesizes a go, pivot, or no-go. Drafts and evaluates; a human ships or kills.

| Function | Role |
|---|---|
| Scopes new ideas, dispatches the panel, synthesizes verdicts into go, pivot, or no-go. | Department Head |
| Cold financial discipline: cap tables, breakeven, ROI, unit economics. Says "I'm out" when the numbers do not work. | Financials |
| Product-market-fit instinct: is this a hero product or a zero, and will the customer pay today. | Product-Market Fit |
| Brand and positioning: naming, the marketing angle, the plan to first customers without a budget. | Brand and Positioning |
| Founder fit and the gut check: is the principal the right person to build this right now, at this life stage. | Founder Fit |
| Tech feasibility and scaling: can it be built, with what stack, in what timeframe, and will it hold past 100 users. | Tech Feasibility |

## Super-User QA: the standing critics (14)

Domain critics, each modeled on a recognized authority in their field, who walk every dashboard from a user's perspective and file tickets against anything that does not hold up. A program manager triages and routes; the principal is removed from the QA loop, and tickets reach the brief only after routing. The people who build the surfaces are never the people who grade them: the resume pipeline's rule, applied to the tools.

| Function | Role |
|---|---|
| QA Program Manager: owns the ticket pipeline end to end. Triages by severity, routes to the owning department, tracks state, auto-closes on confirmation. Cannot fix; pure orchestration. | Program Manager |
| Careers surfaces, from a candidate-experience authority's eye. | Careers Critic |
| Calendar surfaces, from a deep-work and time-management authority's eye. | Calendar Critic |
| Email surfaces, from a batch-it-never-real-time authority's eye. | Email Critic |
| Communications surfaces, from a voice-and-how-it-makes-you-feel authority's eye. | Communications Critic |
| Lifestyle and Operations surfaces, from a does-it-earn-its-place authority's eye. | Lifestyle Critic |
| Fitness surfaces, from a whole-self performance-coach's eye. | Fitness Critic |
| Research surfaces, from a find-the-buried-lede authority's eye. | Research Critic |
| Finance surfaces, from a clarity-honesty-actionability authority's eye. | Finance Critic |
| Dashboard and Tools surfaces, from a visual-display-of-data authority's eye. | Dashboard Critic |
| Learning surfaces, from a deliberate-practice authority's eye: do tips convert, or just pile up. | Learning Critic |
| Social and Marketing surfaces, from a who-is-it-for authority's eye. | Marketing Critic |
| Ventures surfaces, from a leverage-and-unit-economics authority's eye. | Ventures Critic |
| Navigation and information architecture across every department, from a don't-make-me-think authority's eye. | Navigation Critic |

## Totals

3 leadership roles, 12 departments, a 3-agent model-tier routing team, and a 14-agent QA team. The departments carry Careers (23, including the 8-agent case-study studio added 2026-07-11), Research (3), Finance (10), Calendar (3), Email (4), Communications (6), Lifestyle and Operations (7), Fitness (7), Dashboard and Tools (6), Learning (6), Social and Marketing (6), and Entrepreneur (6), for 87 department specialists. With the 3-person leadership layer, the 3-agent model-tier routing team, and the 14-agent QA team, that is 107 named agents in the catalog above, each a single-purpose unit you can actually hold in your head. A 3-agent apex governance layer sits over the whole system as its final quality gate; it decides nothing externally and sends nothing. Counting it, the system runs 110 named agents in all, which is why it is described by the round floor of 100+.
