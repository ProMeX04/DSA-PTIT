def function (n:int, k: int) -> int:
    if n <= k:
        return 2**(n - 1)
    dp = [0] * (n + 1)
    dp[1] = 1
    sum = 1
    for i in range (2, k + 1):
        dp[i] = dp[i - 1] * 2
        sum += dp[i]

    for i in range(k + 1, n + 1):
        dp[i] = sum
        sum += dp[i]
        sum -= dp[i - k]
    return dp[n]



if __name__ == "__main__":
    for i in range(int(input())):
        n, m = map(int, input().split())
        print (function(n, m) % 1000000007)