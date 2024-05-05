
def function():
    n, m, p = map(int, input().split())
    s1, s2, s3 = input().split()

    dp = [[[0] * (p + 1) for i in range(m + 1)] for j in range(n + 1)]
    # dp[n + 1][m + 1][p + 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, p + 1):
                dp[i][j][k] = max(dp[i][j - 1][k],
                                  dp[i][j][k - 1],
                                  dp[i - 1][j][k])
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1] + 1)
    print(dp[n][m][p])


if __name__ == "__main__":
    for i in range(int(input())):
        function()
