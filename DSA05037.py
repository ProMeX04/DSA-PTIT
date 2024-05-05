def function():
    n = int(input())
    dp = [[0] * 100 for i in range(100)]
    for i in range(10):
        dp[0][i] = 1
    for i in range(1, n + 1):
        s = 0
        for j in range(9, -1, -1):
            s += dp[i - 1][j]
            s %= 1000000007
            dp[i][j] = s
    print(dp[n][0])   

if __name__ == "__main__":
    for i in range(int(input())):
        function()