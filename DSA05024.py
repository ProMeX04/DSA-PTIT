
def function():
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))

    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(1,k + 1):
        for j in ls:
            if j <= i:
                dp[i] += dp[i - j] 

    print(dp[k] % 1000000007)
if __name__ == "__main__":
    for i in range(int(input())):
        function()