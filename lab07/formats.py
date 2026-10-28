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

def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_key = None

    for line in lines:
        if "#" in line:
            line = line.split("#", 1)[0]

        if not line.strip():
            continue

        if line.strip().startswith("-"):
            if current_key is not None:
                item_value = line.strip()[1:].strip()
                # Приводим тип элемента списка
                parsed_item = _parse_value(item_value)
                settings[current_key].append(parsed_item)
            continue

        if ":" in line:
            key_part, val_part = line.split(":", 1)
            key = key_part.strip()
            val_str = val_part.strip()

            if val_str == "":
                current_key = key
                settings[current_key] = []
            else:
                current_key = None
                settings[key] = _parse_value(val_str)

    return settings

