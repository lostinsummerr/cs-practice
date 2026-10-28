import json


def csv_to_records(text: str) -> list[dict]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        record = {headers[i]: values[i] for i in range(len(headers))}
        records.append(record)

    return records
