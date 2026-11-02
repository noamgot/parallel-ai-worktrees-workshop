"""Strict shared input validation, not owned by either task."""
import json

SEVERITIES = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")


def read_records(path):
    records = []
    with open(path, encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except ValueError as error:
                raise ValueError("line {}: invalid JSON".format(number)) from error
            if not isinstance(record, dict):
                raise ValueError("line {}: expected an object".format(number))
            if any(not isinstance(record.get(key), str) or not record[key]
                   for key in ("severity", "component", "message")):
                raise ValueError("line {}: severity, component, message must be nonempty strings".format(number))
            if record["severity"] not in SEVERITIES:
                raise ValueError("line {}: unsupported severity".format(number))
            records.append(record)
    return records
