# Demo: a brief that refuses inconsistent numbers, and an approval gate

> **Example type: runnable demonstration with synthetic data.** Standard library Python, no install, no network. It is a simplified implementation of two ideas from this repository. It is **not** the private system, and it does not show how the private hooks work.

## Run it

```bash
python3 demo/run_demo.py          # prints the output below
python3 -m unittest discover -s demo/tests -v    # 12 tests
```

Python 3.9 or newer. The expected output is saved in [expected_output.txt](./expected_output.txt).

## What it demonstrates

| Idea | File | What you will see |
|---|---|---|
| Read department status files and validate their structure | [brief.py](./brief.py), [status/](./status) | Missing fields and bad values are rejected |
| Render a ranked brief | [brief.py](./brief.py) | Red departments first, then every decision that needs a person |
| Refuse inconsistent counts | [brief.py](./brief.py) | A rollup that says 99 open items when the files add up to 13 is refused |
| Block an external action without approval | [approval.py](./approval.py) | The action is queued, not run |
| Approve one exact action, once | [approval.py](./approval.py) | An approval for different arguments does not unlock; a used or expired approval does not unlock |

The "external action" is a stub that returns a string. Nothing is sent anywhere.

## What it does not demonstrate

- The private approval hook, how it is wired into the runtime, or whether every tool and execution path is covered. The demo binds an approval to the exact arguments; I do not claim the private hook does.
- How approval records are protected from edits. In this demo they are plain files that anything with write access could change.
- Agents, models or scheduling. This is the surrounding bookkeeping only.

## About the tests

The tests were also checked by breaking the code on purpose: removing the single-use rule, tying approval to the tool name only, and disabling the rollup check each caused a test to fail. They were then restored.
