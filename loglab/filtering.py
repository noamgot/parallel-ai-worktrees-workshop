"""Task A extension point; see AGENTS.md."""


def filter_records(records, severity=None):
    """Return a new list in input order; exact severity match when supplied."""
    if severity is None:
        return list(records)
    raise NotImplementedError("workshop: implement Task A in loglab/filtering.py")
