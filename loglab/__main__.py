"""CLI owns filter-then-summary composition and deterministic formatting."""
import argparse
import json
import sys

from .filtering import filter_records
from .input import SEVERITIES, read_records
from .summary import summarize_records


def main(argv=None):
    parser = argparse.ArgumentParser(description="Analyze synthetic JSON Lines logs")
    parser.add_argument("path", help="UTF-8 JSON Lines file")
    parser.add_argument("--severity", choices=SEVERITIES)
    parser.add_argument("--summary", action="store_true", help="count filtered records by component")
    args = parser.parse_args(argv)
    try:
        records = filter_records(read_records(args.path), args.severity)
        if args.summary:
            counts = summarize_records(records)
            output = ["{}: {}".format(component, counts[component]) for component in sorted(counts)]
        else:
            output = [json.dumps(record, sort_keys=True, ensure_ascii=False) for record in records]
    except (OSError, UnicodeError, ValueError, NotImplementedError) as error:
        print("loglab: {}".format(error), file=sys.stderr)
        return 2
    for line in output:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
