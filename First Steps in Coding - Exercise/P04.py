page_count = int(input())
page_per_hour = int(input())
days = int(input())

hours_needed = int((page_count / page_per_hour) / days)
print(hours_needed)