# The application pipeline

The highest-stakes workflow in the system. A single role passes through 14 agents before anything reaches a human review queue. The shape is **attack → defend → validate → decide**: build it, hand it to critics whose only job is to break it, repair, validate against a checklist, and judge it as a whole.

Nothing is ever submitted automatically. The pipeline's entire job is to produce a package a human can review and send with confidence.

## The stages

**1 · Strategy / positioning.** Before a word is written, a strategy lead reads the job description and produces a positioning brief: which variant of the candidate's background to lead with, the top themes the company values, the hidden priorities between the lines, and an honest read on where the fit is a stretch. Every downstream agent works from this brief.

**2 · Drafting (parallel).** Three agents work at once: a résumé tailor that mirrors the JD's language where truthful, a cover-letter writer, and a company-intel agent that surfaces named contacts and warm paths. The résumé holds a single locked canonical format; only wording is tailored per role.

**3–6 · Adversarial review (parallel).** The package is handed to four independent critics, each blind to the others:

- **Coverage**. Scores the résumé's keyword coverage against the JD's applicant-tracking requirements and kicks it back below threshold.
- **Truthfulness**. Audits every claim for fabrication, inflated metrics, and borrowed pedigree (implying experience the candidate doesn't have). Anything that wouldn't survive interview cross-examination is rejected. This is a hard gate.
- **Skeptic**. Reads the finished package the way a busy recruiter does in the first 15 seconds, scanning for reasons to put it down, and names the single most likely rejection.
- **Red-team**. Argues the worst-case interpretation: logical gaps, cross-document contradictions, interview trap-doors.

The agent that *wrote* the document is never one of the agents that *grades* it.

**7 · Humanization.** A dedicated editor rewrites for varied rhythm and broken parallelism so the output reads like a high-performing human wrote it. AI-generated writing has a detectable style; a banned-phrase list is not enough, so this is a real stage, not a find-and-replace.

**8 · QC validation.** A multi-gate checklist pass: document structure, ATS, executive presence, format adherence, voice, and a long list of house style rules. Minor issues are fixed in place; major ones are kicked back to the named agent responsible, with instructions.

**9 · Committee.** A final holistic go/no-go. A document can pass every individual gate and still be wrong as a whole: too generic, mispositioned, off-narrative. The committee makes the judgment call the checklists can't.

**Loop.** Any kickback returns the package to the relevant stage with notes attached. A role only advances when it survives every gate *and* the committee.

## What reaches the human

A role surfaces to the review queue only when it is both fully QC'd **and** committee-approved, with submittable files actually rendered on disk. Then a person opens the portal, reviews, and clicks submit. The system prepares; the human decides.

## Why it's shaped this way

- **Separate the auditor from the author.** Writers grade their own work too kindly. ATS scoring, truthfulness, and recruiter-perception are different agents from the ones who wrote the document.
- **Make optimism argue with skepticism.** A single voice (however good) converges on its own blind spots. The red-team and the skeptic exist to disagree.
- **Truthfulness is non-negotiable.** The fastest way to lose a candidate's trust is a package that doesn't survive the interview. The truthfulness gate is the one no other agent can override.
- **Decide as a whole, last.** Holistic judgment comes after the checklists, never instead of them.
