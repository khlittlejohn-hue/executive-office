# Hook: the approval gate

> **Example type: pseudocode.** This is a simplified sketch of the idea, not the private implementation and not runnable. It does not prove that the private system cannot be bypassed. It shows the design intent so a reader can judge it.

An example of a `PreToolUse` hook, sanitized. In Claude Code, hooks are commands the runtime runs at defined points, such as before a tool call. A hook runs as code in the execution path, so it does not depend on an agent following its prompt.

## What it is designed to do

Before a tool call that would affect the outside world (send an email, submit a form, write to a calendar), the hook checks for a one-time approval. If there is none, it records the attempted action in an approval queue and blocks the call. A person approves from that queue, one item at a time. Approvals are not standing and are not inferred.

## Shape

```
on PreToolUse(tool, args):
    if tool matches an external-effect pattern:       # send / submit / external write
        if a one-time approval exists for this tool:
            consume it                                 # a used approval is not reused
            return ALLOW
        queue_for_human(tool, args, expires_in=7_days)
        return BLOCK("external action requires explicit human approval")
    return ALLOW
```

## Instruction versus enforcement

These are different things, and the system uses all of them:

| Layer | What it is | Can it be skipped by the agent? |
|---|---|---|
| Prompt instruction | Text telling an agent not to take external actions | Yes. A model can misread or ignore it. |
| Tool permissions | Which tools an agent is given at all | No, for a tool it was not given. A reviewer given a write tool can still write; an instruction to "only review" is not a permission boundary. |
| Runtime hook | Code that runs before a tool call and can block it | Only if the hook is absent, misconfigured, or the call uses a path the hook does not cover. |
| Interface | The human-facing approval queue | It records and presents decisions. It does not stop a tool by itself. |

The design relies on the runtime hook and the human queue for the external-action rule, and treats the prompt as a first line that reduces how often the hook has to fire.

## What this example does not show

The public sketch does not demonstrate, and this repository does not claim to prove:

- how an approval is tied to the exact action and arguments that were approved (the [runnable demo](../demo) binds approval to the exact arguments, and I do not claim the private hook does)
- how expiry and reuse are handled in edge cases
- that every tool and every alternative execution path is covered
- how the approval record itself is protected from edits

The private hook is not published. Describing it here is a statement of design intent, not independent evidence. The [claim-to-evidence inventory](../docs/EVIDENCE.md) lists what can and cannot be inspected from this repository.

## Platform note

The behavior described is for Claude Code hooks as observed in my own configuration. Hook semantics are defined by the runtime and can change between versions, so check the current Claude Code documentation before relying on any detail here.
