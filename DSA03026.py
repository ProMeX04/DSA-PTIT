def MAX(n, s):
    arr = [0] * n
    i = 0
    while s:
        arr[i] = 9 if s >= 9 else s
        s -= arr[i]
        i += 1
    res = 0
    for i in range(n):
        res = res * 10 + arr[i]
    return res


def MIN(n, s):
    arr = [0] * n
    s -= 1
    i = n - 1
    while s:
        arr[i] = 9 if s >= 9 else s
        s -= arr[i]
        i -= 1
    res = 0
    arr[0] += 1
    for i in range(n):
        res = res * 10 + arr[i]
    return res


def check(n, s):
    return n > 0 and s <= n * 9 and s > 0


def function():
    n, s = map(int, input().split())
    if s == 0 and n == 0:
        print(0, 0)
        return

    
    if check(n, s):
        print(MIN(n, s), MAX(n, s))
    else:
        print(-1, -1)


if __name__ == "__main__":
    function()
