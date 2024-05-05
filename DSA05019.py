
def function():
    n, m = map (int, input().split())
    matrix = [list(map(int, input().split())) for i in range(n)]
    dp = [[0] * (m + 1) for i in range(n + 1)]
    result = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i - 1][j - 1]:
                dp[i][j] = min (dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            result = max(dp[i][j], result)

    print(result)
if __name__ == "__main__":
    for i in range(int(input())):
        function()