"""Task A extension point; see AGENTS.md."""


def filter_records(records, severities=None, components=None, message=None):
    """Return a new list in input order, without mutating the input.

    None disables a filter; empty severity/component collections match nothing.
    Match either value within each collection, and require all active filters.
    Severity/component matches are exact and case-sensitive. Message is a
    case-sensitive substring (the empty string matches every message).
    Inputs are already validated; do not normalize or validate them here.
    """
    if severities is None and components is None and message is None:
        return list(records)
    raise NotImplementedError("workshop: implement Task A in loglab/filtering.py")
