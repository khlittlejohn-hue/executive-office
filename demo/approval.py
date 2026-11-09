"""Approval gate demo: an external action is blocked unless a person has approved
that exact action, once, before it expires.

Standard library only. The 'external action' here is a stub that only returns a
string, so nothing is sent anywhere. This is a demonstration of the pattern in
the repository's hook example. It is NOT the private hook, and it does not show
how the private system binds approvals.
"""
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path

EXTERNAL_TOOLS = {"send_email", "submit_form", "write_calendar"}
EXPIRY = timedelta(days=7)


def action_id(tool, args):
    """The identity of an action is its tool plus its exact arguments."""
    blob = json.dumps({"tool": tool, "args": args}, sort_keys=True).encode()
    return hashlib.sha256(blob).hexdigest()[:16]


class Queue:
    def __init__(self, root):
        self.root = Path(root)
        (self.root / "pending").mkdir(parents=True, exist_ok=True)
        (self.root / "approved").mkdir(parents=True, exist_ok=True)

    def add_pending(self, tool, args, now):
        aid = action_id(tool, args)
        item = {"id": aid, "tool": tool, "args": args, "queued": now.isoformat(),
                "expires": (now + EXPIRY).isoformat()}
        (self.root / "pending" / (aid + ".json")).write_text(json.dumps(item, indent=2))
        return aid

    def approve(self, aid):
        """A person approves one queued item. Nothing else grants approval."""
        src = self.root / "pending" / (aid + ".json")
        item = json.loads(src.read_text())
        (self.root / "approved" / (aid + ".json")).write_text(json.dumps(item, indent=2))
        src.unlink()

    def consume(self, aid, now):
        """Use an approval once. Returns True only for a live, unused approval."""
        path = self.root / "approved" / (aid + ".json")
        if not path.exists():
            return False
        item = json.loads(path.read_text())
        path.unlink()  # single use, whether or not it turns out to be expired
        return now <= datetime.fromisoformat(item["expires"])


def guarded_call(tool, args, queue, now, action):
    """Run `action` only if the tool is internal or this exact action is approved."""
    if tool not in EXTERNAL_TOOLS:
        return "ALLOWED (internal): " + action(**args)
    aid = action_id(tool, args)
    if queue.consume(aid, now):
        return "ALLOWED (approved %s): %s" % (aid, action(**args))
    aid = queue.add_pending(tool, args, now)
    return "BLOCKED: queued for human approval as %s" % aid


def fake_send(to, subject):
    return "would send '%s' to %s (stub, nothing sent)" % (subject, to)
