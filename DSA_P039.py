def solve(a, n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                dp[i][j] = a[j]
            else:
                dp[i][j] = max(dp[i - 1][k] + a[k][j] for k in range(j))
    return max(dp[n - 1])

# Đọc input
t = int(input())
for _ in range(t):
    n = int(input())
    a = [[int(x) for x in input().split()] for _ in range(n)]
    res = solve(a, n)
    print(res)
