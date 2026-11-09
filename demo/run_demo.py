"""Run the whole demonstration with synthetic data. No network, no external actions."""
import shutil
import tempfile
from datetime import datetime
from pathlib import Path

import approval
import brief

HERE = Path(__file__).parent
NOW = datetime(2026, 1, 12, 7, 15)

print("== 1. Build the brief from the status files ==")
text, problems = brief.build(HERE / "status")
print(text)

print("\n== 2. A rollup that disagrees with its sources is refused ==")
tmp = Path(tempfile.mkdtemp())
try:
    shutil.copytree(HERE / "status", tmp / "status")
    (tmp / "status" / "_rollup.json").write_text('{"departments": 4, "open_items": 99, "decisions_needed": 4}')
    _, problems = brief.build(tmp / "status")
    print("REFUSING TO RENDER:" if problems else "unexpectedly rendered")
    for p in problems:
        print("  - " + p)

    print("\n== 3. An external action without approval is blocked ==")
    q = approval.Queue(tmp / "queue")
    args = {"to": "vendor@example.com", "subject": "Renewal"}
    print(approval.guarded_call("send_email", args, q, NOW, approval.fake_send))

    print("\n== 4. A person approves that exact action, and it runs once ==")
    q.approve(approval.action_id("send_email", args))
    print(approval.guarded_call("send_email", args, q, NOW, approval.fake_send))
    print(approval.guarded_call("send_email", args, q, NOW, approval.fake_send))
finally:
    shutil.rmtree(tmp)
