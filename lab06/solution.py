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
