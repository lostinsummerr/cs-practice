import csv
import io
import json


def csv_to_records(text: str) -> list[dict]:

    f = io.StringIO(text.strip())
    reader = csv.DictReader(f)
    return [row for row in reader if row]

def parse_settings(lines: list[str]) -> dict:

    def parse_value(v: str):
        v = v.strip()
        if v.lower() in ("true", "yes"):
            return True
        if v.lower() in ("false", "no"):
            return False
        try:
            return int(v)
        except ValueError:
            pass
        try:
            return float(v)
        except ValueError:
            pass
        return v
    result = {}
    current_list_key = None

    for line in lines:
        if "#" in line:
            line = line.split("#", 1)[0]

        
        stripped = line.strip()
        if not stripped:
            continue

      
        if stripped.startswith("-"):
            if current_list_key is not None:
                val = stripped[1:].strip()  
                result[current_list_key].append(parse_value(val))
            continue

        
        current_list_key = None


        if ":" in stripped:
            key, val = stripped.split(":", 1)
            key = key.strip()
            val = val.strip()

            if val == "":
                
                current_list_key = key
                result[current_list_key] = []
            else:

                result[key] = parse_value(val)

    return result
def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    merged_rows = []
    for row in rows:
        new_row = row.copy()

        lookup_val = str(row.get(key, ""))

        if lookup_val in extra:
            extra_data = extra[lookup_val]
            for k, v in extra_data.items():
                if k not in new_row:
                    new_row[k] = v

        merged_rows.append(new_row)
    return merged_rows
def records_to_json(records: list[dict]) -> str:
    return json.dumps(
        records,
        sort_keys=True,  
        indent=2,
        ensure_ascii=False,
