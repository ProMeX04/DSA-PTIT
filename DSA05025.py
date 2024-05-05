


def function(n: int) -> int:
    dp = [0] * (max(4, n + 1))
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i-2] + dp[i - 3]
    return dp[n]


if __name__ == "__main__":
    for i in range(int (input())):
        n = int(input())
        print(function(n))
