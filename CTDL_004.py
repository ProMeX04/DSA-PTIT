


def function (): 
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    dp = [[0] * (k) for i in range(n)]
    for i in range(n):
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                for l in range(1,k):
                    dp[i][l] += dp[j][l-1]

    ans = 0
    for i in range(n):
        ans += dp[i][k - 1]
    print (ans)
if __name__ == "__main__":
    function()