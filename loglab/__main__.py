"""CLI owns filter-then-summary composition and deterministic formatting."""
import argparse
import json
import sys

from .filtering import filter_records
from .input import SEVERITIES, read_records
from .summary import summarize_records


def nonnegative_int(value):
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be nonnegative")
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description="Analyze synthetic JSON Lines logs")
    parser.add_argument("path", help="UTF-8 JSON Lines file")
    parser.add_argument("--severity", choices=SEVERITIES, action="append")
    parser.add_argument("--component", action="append", help="exact component (repeatable)")
    parser.add_argument("--message", help="case-sensitive message substring")
    parser.add_argument("--summary", action="store_true", help="count filtered records by component")
    parser.add_argument("--top", type=nonnegative_int, help="limit summary to N components")
    args = parser.parse_args(argv)
    if args.top is not None and not args.summary:
        parser.error("--top requires --summary")
    try:
        records = read_records(args.path)
        # TODO (human-led integration): pass filter options to filter_records,
        # then summarize_records(top_n=args.top) when requested. Format summaries
        # as `api: total=3 ERROR=2 INFO=1`, sorting severity keys alphabetically.
        # Preserve summary ranking and emit no lines for an empty result.
        if (args.severity is not None or args.component is not None
                or args.message is not None or args.summary):
            raise NotImplementedError("workshop: CLI integration required (filter/summary options)")
        records = filter_records(records)
        output = [json.dumps(record, sort_keys=True, ensure_ascii=False) for record in records]
    except (OSError, UnicodeError, ValueError) as error:
        print("loglab: {}".format(error), file=sys.stderr)
        return 2
    for line in output:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
