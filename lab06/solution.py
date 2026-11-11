def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        filename = path.split("/")[-1]
        
        if "." not in filename:
            ext = ""
        elif filename.startswith(".") and "." not in filename[1:]:
            ext = ""  # скрытый файл без расширения типа .gitignore
        else:
            ext = filename.rsplit(".", 1)[1].lower()
        
        counts[ext] = counts.get(ext, 0) + 1
    
    return counts

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    
    max_depth = -1
    result = ""
    
    for path in paths:
        depth = path.count("/")
        
        if depth > max_depth or (depth == max_depth and path < result):
            max_depth = depth
            result = path
    
    return result

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    
    value = float(n_bytes)
    for unit in units[1:]:
        value /= 1024
        if value < 1024 or unit == "ТБ":
            return f"{value:.1f} {unit}"
