
def function():
    n = int(input())
    value = [0] + list(map(int, input().split())) + [0, 0]
    dp = [0] * (n + 1)
    for i in range(n + 1):
        dp[i] = max(dp[i - 2] + value[i], dp[i - 1])
    print(max(dp))


if __name__ == "__main__":
    for i in range(int(input())):
        function()
