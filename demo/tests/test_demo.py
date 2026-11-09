import json
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import approval  # noqa: E402
import brief  # noqa: E402

NOW = datetime(2026, 1, 12, 7, 15)
ARGS = {"to": "vendor@example.com", "subject": "Renewal"}


class TestBrief(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copytree(HERE / "status", self.tmp / "status")
        self.status = self.tmp / "status"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_fixtures_are_valid_json_and_pass_validation(self):
        for name, s in brief.load_statuses(self.status):
            self.assertEqual(brief.validate(name, s), [], name)

    def test_brief_ranks_red_first_and_lists_every_decision(self):
        text, problems = brief.build(self.status)
        self.assertEqual(problems, [])
        status_lines = [l for l in text.splitlines() if l.startswith("  RED") or l.startswith("  YELLOW") or l.startswith("  GREEN")]
        self.assertTrue(status_lines[0].startswith("  RED"))
        for decision_id in ("cal-01", "mail-01", "mail-02", "fin-01"):
            self.assertIn(decision_id, text)

    def test_missing_field_is_rejected(self):
        p = self.status / "email.json"
        d = json.loads(p.read_text())
        del d["blockers"]
        p.write_text(json.dumps(d))
        text, problems = brief.build(self.status)
        self.assertIsNone(text)
        self.assertTrue(any("missing 'blockers'" in x for x in problems))

    def test_bad_ryg_value_is_rejected(self):
        p = self.status / "calendar.json"
        d = json.loads(p.read_text())
        d["ryg"] = "purple"
        p.write_text(json.dumps(d))
        _, problems = brief.build(self.status)
        self.assertTrue(any("ryg must be" in x for x in problems))

    def test_inconsistent_rollup_is_refused(self):
        (self.status / "_rollup.json").write_text('{"departments": 4, "open_items": 99, "decisions_needed": 4}')
        text, problems = brief.build(self.status)
        self.assertIsNone(text)
        self.assertEqual(len(problems), 1)
        self.assertIn("open_items", problems[0])

    def test_consistent_rollup_renders(self):
        text, problems = brief.build(self.status)
        self.assertEqual(problems, [])
        self.assertIn("4 departments, 13 open items, 4 decisions need you", text)


class TestApproval(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.q = approval.Queue(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def call(self, args=ARGS, now=NOW, tool="send_email"):
        return approval.guarded_call(tool, args, self.q, now, approval.fake_send)

    def test_internal_tool_is_allowed_without_approval(self):
        r = approval.guarded_call("write_notes", {"to": "x", "subject": "y"}, self.q, NOW, approval.fake_send)
        self.assertTrue(r.startswith("ALLOWED (internal)"))

    def test_external_action_without_approval_is_blocked_and_queued(self):
        self.assertTrue(self.call().startswith("BLOCKED"))
        self.assertEqual(len(list((self.tmp / "pending").glob("*.json"))), 1)

    def test_approval_unlocks_once_then_blocks_again(self):
        self.call()
        self.q.approve(approval.action_id("send_email", ARGS))
        self.assertTrue(self.call().startswith("ALLOWED (approved"))
        self.assertTrue(self.call().startswith("BLOCKED"))

    def test_approval_for_different_arguments_does_not_unlock(self):
        self.call()
        self.q.approve(approval.action_id("send_email", ARGS))
        other = {"to": "someone-else@example.com", "subject": "Renewal"}
        self.assertTrue(self.call(args=other).startswith("BLOCKED"))

    def test_expired_approval_is_rejected_and_consumed(self):
        self.call()
        self.q.approve(approval.action_id("send_email", ARGS))
        late = NOW + approval.EXPIRY + timedelta(seconds=1)
        self.assertTrue(self.call(now=late).startswith("BLOCKED"))

    def test_nothing_is_actually_sent(self):
        self.call()
        self.q.approve(approval.action_id("send_email", ARGS))
        self.assertIn("stub, nothing sent", self.call())


if __name__ == "__main__":
    unittest.main()
