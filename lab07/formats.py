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
def _parse_value(val_str: str):
    val_str = val_str.strip()
    if val_str.lower() in ("true", "yes"):
        return True
    if val_str.lower() in ("false", "no"):
        return False
    try:
        return int(val_str)
    except ValueError:
        pass
    try:
        return float(val_str)
    except ValueError:
        pass
    return val_str
