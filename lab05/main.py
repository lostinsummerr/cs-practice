import os
from logstats import count_levels, top_errors, format_report

def main():
    filename = input().strip()
    
    with open(filename, encoding="utf-8") as log:
        counts = count_levels(log)
        
    with open(filename, encoding="utf-8") as log:
        errors = top_errors(log, 3)
        
    total_lines = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)
    
    print(total_lines)
    print(error_count)
    print(broken_count)
    
    report_text = format_report(counts, errors)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(script_dir, "report.txt")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)

if __name__ == "__main__":
    main()
