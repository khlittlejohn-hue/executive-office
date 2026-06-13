# Hook — the approval gate, enforced at runtime

An example of a `PreToolUse` hook, sanitized. Hooks fire deterministically at defined points in the runtime, so they enforce a rule even if an agent's prompt is ignored or worked around. This is the load-bearing layer of the human-in-the-loop guarantee.

## What it does

Before any tool call that would touch the outside world (send an email, submit a form, write to a calendar), this hook intercepts the call and blocks it unless a per-action approval flag is present. Approval is granted by a human, one action at a time, from a queue — never standing, never inferred.

## Shape

```
on PreToolUse(tool, args):
    if tool is an external-effect tool:               # send / submit / external write
        approval = read_approval_flag(action_id(args))
        if not approval or approval.granted_by != "human":
            return BLOCK("external action requires explicit human approval")
    return ALLOW
```

## Why a hook and not a prompt

- **Prompts are advice; hooks are law.** Every agent is also told not to take external actions, but a prompt can be misread, jailbroken, or simply forgotten across a long context. The hook cannot be talked out of it — it is code in the execution path.
- **Defense in depth.** This is one of three independent layers (prompt instruction, this runtime hook, and a human-only approval queue in the interface). A single missed check at any one layer does not leak an external action.
- **Internal work stays fast.** The hook only guards external-effect tools. Editing files, rendering dashboards, and drafting documents flow freely under a standing internal authority, so the gate never slows the system down where it doesn't need to.

## The principle

The most important rule in the system — nothing reaches the outside world without a human — is the one rule that gets its own enforcement mechanism, in the runtime, where no prompt can override it.
