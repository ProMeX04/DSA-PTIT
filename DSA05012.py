def function(n:, k: int) -> int:
    dp = [[1 for i in range(k + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1 , k + 1):
            if i == j or j == 0:
                dp[i][j] = 1
            elif j > i:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                dp[i][j] %= 1000000007

    return dp[n][k]

def main():
    for i in range(int(input())):
        n, k = map(int, input().split())
        print (function(n, k))


if __name__ == "__main__":
    main()
