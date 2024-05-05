
def function():
    n = int(input())
    A, B  = [0] * n, [0] * n
    for i in range(n):
        A[i], B[i] = map(float, input().split())

    dp = [0] * (n + 1)

    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if A[j] < A[i] and B[j] > B[i]:
                dp[i] = max(dp[j] + 1, dp[i]) 

    print(max(dp))
if __name__ == "__main__":
    for i in range(int(input())):
        function()