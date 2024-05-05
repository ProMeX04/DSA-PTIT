def function(*line, **kwarg):
    n, A = line

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        dp[i] = 1
        if A[i] > A[i - 1]:
            dp[i] = dp[i - 1] + 1

    dp1 = [0] * (n + 1)
    dp1[n - 1] = 1
    for i in range(n - 2, -1, -1):
        dp1[i] = 1
        if A[i] > A[i + 1]:
            dp1[i] = dp1[i + 1] + 1

    return max([a + b - 1 for a, b in zip(dp, dp1)])


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()),  list(map(int, input().split()))))
