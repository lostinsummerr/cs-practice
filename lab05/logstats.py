def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")
    
    parts = line.split(maxsplit=2)
    
    if len(parts) < 3:
        raise ValueError("Не хватает частей (времени, уровня или сообщения)")
        
    time_str, level, message = parts
    
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")
        
    return {"time": time_str, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"
            
        counts[level] = counts.get(level, 0) + 1
        
    return counts
def top_errors(lines, n: int) -> list:
    error_counts = {}
    
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue

    # Сортируем: сначала по убыванию количества (-x[1]), 
    # затем по алфавиту сообщения (x[0])
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    
    return [[msg, count] for msg, count in sorted_errors[:n]]
