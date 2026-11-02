"""Task B extension point; see AGENTS.md."""


def summarize_records(records, top_n=None):
    """Return ranked component dictionaries without mutating records.

    Each dictionary has component (str), total (int), and severities (a mapping
    of observed severity names to counts, with no zero-count entries).
    Sort by total descending, then component ascending, case-sensitively.
    top_n=None returns all groups; 0 returns []; positive N returns first N.
    Callers supply nonnegative integers; do not add input validation.
    """
    raise NotImplementedError("workshop: implement Task B in loglab/summary.py")
