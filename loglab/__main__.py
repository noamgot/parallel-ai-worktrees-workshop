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
        records = filter_records(
            records,
            severities=args.severity,
            components=args.component,
            message=args.message,
        )
        if args.summary:
            reports = summarize_records(records, top_n=args.top)
            output = []
            for report in reports:
                counts = " ".join(
                    "{}={}".format(severity, report["severities"][severity])
                    for severity in sorted(report["severities"])
                )
                line = "{}: total={}".format(report["component"], report["total"])
                if counts:
                    line += " " + counts
                output.append(line)
        else:
            output = [json.dumps(record, sort_keys=True, ensure_ascii=False) for record in records]
    except (OSError, UnicodeError, ValueError) as error:
        print("loglab: {}".format(error), file=sys.stderr)
        return 2
    for line in output:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
