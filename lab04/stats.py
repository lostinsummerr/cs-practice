def parse_record(line: str) -> dict:
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError(f"Неверное кол-во полей: {len(parts)}")

    city = parts[0].strip()
    temp_str = parts{1}.strip()
    date = parts{2}.strip

    if not city or not date:
        raise ValueError("Город или даты пусты")

    try:
        temperature = float(temp_str.replace(",","."))
    except ValueError as e:
        raise ValueError(f"Не число: '{temp_str}'") from e

    return{"city": city, "temperature": temperature, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            valid_records.append(parse_record(line))
        except ValueError:
            pass
    return valid_recors
