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

def average_by_city(records: list[dict]) -> dict:
    if not records:
        return {}
    totals = {}
    counts = {}
    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]
        totals[city] = totals.get(city, 0.0) + temp
        counts[city] = counts.get(city, 0) + 1
    return {city: round(totals[city] / counts[city], 1) for city in totals}


def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    averages = average_by_city(records)
    max_temp = max(averages.values())
    warmest = [city for city, temp in averages.items() if temp == max_temp]
    return sorted(warmest)[0]