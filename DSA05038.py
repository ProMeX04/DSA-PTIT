import collections

def add(time_history, x, y):
    for dct in time_history:
        if x in dct and dct[x] >= y:
            dct.pop(x)  # Remove if equal or greater
    time_history[-1][x] = y

def check(time_history, x, y):
    for i in range(len(time_history) - 1, -1, -1):  # Check in reverse order
        if x in time_history[i] and time_history[i][x] < y:
            return True
    return False

n = int(input())
time_history = [collections.defaultdict(int)]  # List of dictionaries

result = 0
for _ in range(n):
    x, y = map(int, input().split())

    l, r = 0, result
    while l <= r:
        mid = (l + r) // 2
        if check(time_history, x, y):
            l = mid + 1
        else:
            r = mid - 1

    if result == l - 1:
        result = l
    add(time_history, x, y)
    time_history.append(time_history[-1].copy())  # Add a new level

print(result)
