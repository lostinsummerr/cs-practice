import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    records = read_valid(lines)
    valid_count = len(records)
    
    non_empty_count = sum(1 for line in lines if line.strip())
    error_count = non_empty_count - valid_count
    
    if records:
        warmest = warmest_city(records)
        max_temp = average_by_city(records)[warmest]
    else:
        max_temp = 0.0

    print(valid_count)
    print(error_count)
    print(f"{max_temp:.1f}")

if __name__ == "__main__":
    main()