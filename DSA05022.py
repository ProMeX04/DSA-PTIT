
def function():
    n = int(input())
    x, y, z = map(int, input().split())

    dp = [0] * (n + 1)
    dp[1] = x
    dp[2] = x + min(x, z)

    for i in range(3, n + 1):
        dp[i] = min(dp[(i + 1) // 2] + z + (i % 2) * y, dp[i - 1] + x)

    print(dp[n])


if __name__ == "__main__":
    for i in range(int(input())):
        function()
