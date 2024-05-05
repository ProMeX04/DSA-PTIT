
def function():
    n = int(input())
    ls = list(map(int, input().split()))

    dp = [0] * n
    for i in range(n):
        dp[i] = max(dp[i - 1], dp[i - 2] + ls[i])
    print(max(dp))

if __name__ == "__main__":
    for i in range(int(input())):
        function()