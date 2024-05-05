from array import *


def function(n: int, k: int) -> int:
    mod = 1000000007
    if n <= k:
        return 2**(n - 1) % mod

    dp = [0 for i in range(n + 1)]

    sum = 0
    for i in range(1, k + 1):
        dp[i] = 2**(i - 1) % mod
        dp[i] %= mod
        sum += dp[i]
        sum %= mod

    for i in range(k + 1, n + 1):
        dp[i] = sum
        sum -= dp[i - k]
        sum += dp[i]
        sum %= mod

    return dp[n]


def main():
    for i in range(int(input())):
        n, k = map(int, input().split())
        print(function(n, k))


if __name__ == "__main__":
    main()
