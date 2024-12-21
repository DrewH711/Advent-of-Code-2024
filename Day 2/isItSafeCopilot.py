def is_safe(report):
    levels = list(map(int, report.split()))
    increasing = all(levels[i] < levels[i+1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i+1] for i in range(len(levels) - 1))
    valid_diff = all(1 <= abs(levels[i] - levels[i+1]) <= 3 for i in range(len(levels) - 1))
    
    return (increasing or decreasing) and valid_diff

def count_safe_reports(data):
    reports = data.strip().split('\n')
    safe_count = sum(is_safe(report) for report in reports)
    return safe_count

# Example input data
test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

# Count the safe reports
safe_reports_count = count_safe_reports(test_data)
print(safe_reports_count)