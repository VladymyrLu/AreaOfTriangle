def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))
print(sum_range(4, 1))

