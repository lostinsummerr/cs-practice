def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: {len(parts)}")
    
    city = parts[0].strip()
    temp_str = parts[1].strip().replace(",", ".")
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Город или дата пустые")
    
    try:
        temperature = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура не является числом: '{parts[1].strip()}'")
    
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue 
        try:
            valid_records.append(parse_record(line))
        except ValueError:
            pass  
    return valid_records