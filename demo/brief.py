"""Executive brief demo: read synthetic department status files, validate them,
check that a rollup agrees with the sources, and render a ranked brief.

Standard library only. All data here is synthetic. This is a small
demonstration of the pattern; it is not the private system.
"""
import json
import sys
from pathlib import Path

REQUIRED = {
    "department": str, "lastUpdated": str, "ryg": str, "headline": str,
    "metrics": dict, "blockers": list, "needsDecision": list,
}
RYG_ORDER = {"red": 0, "yellow": 1, "green": 2}


class StatusError(ValueError):
    pass


def load_statuses(directory):
    """Load every department status file (files starting with '_' are not departments)."""
    out = []
    for path in sorted(Path(directory).glob("*.json")):
        if path.name.startswith("_"):
            continue
        out.append((path.name, json.loads(path.read_text())))
    return out


def validate(name, status):
    """Return a list of problems with one status file (empty list means valid)."""
    problems = []
    for key, typ in REQUIRED.items():
        if key not in status:
            problems.append("%s: missing '%s'" % (name, key))
        elif not isinstance(status[key], typ):
            problems.append("%s: '%s' should be %s" % (name, key, typ.__name__))
    if status.get("ryg") not in RYG_ORDER and "ryg" in status:
        problems.append("%s: ryg must be one of %s" % (name, sorted(RYG_ORDER)))
    if isinstance(status.get("metrics"), dict) and not isinstance(status["metrics"].get("open_items"), int):
        problems.append("%s: metrics.open_items must be an integer" % name)
    return problems


def totals(statuses):
    """Counts computed from the sources, never typed in by hand."""
    return {
        "departments": len(statuses),
        "open_items": sum(s["metrics"]["open_items"] for _, s in statuses),
        "decisions_needed": sum(len(s["needsDecision"]) for _, s in statuses),
    }


def check_rollup(statuses, rollup):
    """Return mismatches between a rollup's claimed counts and the source files."""
    actual = totals(statuses)
    return ["rollup says %s=%s but the department files add up to %s" % (k, rollup.get(k), v)
            for k, v in actual.items() if rollup.get(k) != v]


def render_brief(statuses):
    """Rank departments red first; list every decision the human must make."""
    ranked = sorted(statuses, key=lambda p: (RYG_ORDER[p[1]["ryg"]], p[1]["department"]))
    t = totals(statuses)
    lines = ["EXECUTIVE BRIEF (synthetic data)",
             "%d departments, %d open items, %d decisions need you" % (t["departments"], t["open_items"], t["decisions_needed"]),
             "", "DECISIONS"]
    n = 0
    for _, s in ranked:
        for d in s["needsDecision"]:
            n += 1
            lines.append("  %d. [%s] %s (%s)" % (n, s["department"], d["text"], d["id"]))
    if n == 0:
        lines.append("  none")
    lines += ["", "STATUS"]
    for _, s in ranked:
        lines.append("  %-6s %-9s %s" % (s["ryg"].upper(), s["department"], s["headline"]))
        for b in s["blockers"]:
            lines.append("           blocked: %s" % b)
    return "\n".join(lines)


def build(directory):
    """Validate, check the rollup, and return (brief_text, problems)."""
    statuses = load_statuses(directory)
    problems = [p for name, s in statuses for p in validate(name, s)]
    if problems:
        return None, problems
    rollup_path = Path(directory) / "_rollup.json"
    if rollup_path.exists():
        problems = check_rollup(statuses, json.loads(rollup_path.read_text()))
        if problems:
            return None, problems
    return render_brief(statuses), []


if __name__ == "__main__":
    brief, problems = build(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "status")
    if problems:
        print("REFUSING TO RENDER: the data is inconsistent")
        for p in problems:
            print("  - " + p)
        sys.exit(1)
    print(brief)
