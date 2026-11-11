import json

def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().split("\n")
    if not lines or lines == [""]:
        return []
    
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        record = {}
        for i, header in enumerate(headers):
            record[header] = values[i] if i < len(values) else ""
        records.append(record)
    
    return records

def parse_value(value: str):
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False
    
    try:
        return int(value)
    except ValueError:
        pass
    
    try:
        return float(value)
    except ValueError:
        pass
    
    if "," in value:
        try:
            return float(value.replace(",", "."))
        except ValueError:
            pass
    
    return value


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_key = None
    current_list = None
    
    for line in lines:
        if "#" in line:
            line = line[:line.index("#")]
        
        line = line.rstrip()
        
        if not line:
            continue
        
        stripped = line.strip()
        if stripped.startswith("- "):
            value = stripped[2:].strip()
            if current_key is not None:
                current_list.append(parse_value(value))
            continue
        
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            
            if value == "":
                current_key = key
                current_list = []
                result[key] = current_list
            else:
                current_key = None
                current_list = None
                result[key] = parse_value(value)
    
    return result

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        key_value = row.get(key)
        if key_value in extra:
            merged = {**extra[key_value], **row}
            result.append(merged)
        else:
            result.append(row.copy())
    return result

def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, sort_keys=True, indent=2, ensure_ascii=False)
