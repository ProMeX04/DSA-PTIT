
def function():
    n = int(input())
    ls = list(map(int, input().split()))

    dp = [0] * n 
    for i in range(n):
        dp[i] = ls[i]
        for j in range(i):
            if ls[i] > ls[j]:
                dp[i] = max(dp[j] + ls[i], dp[i])

    print(max(dp))

if __name__ == "__main__":
    for i in range(int(input())):
        function()