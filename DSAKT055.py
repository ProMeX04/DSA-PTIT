
def function():
    n, V = map(int, input().split())
    w = list(map(int, input().split()))
    c = list(map(int, input().split()))
    product = [(a, b) for a, b in zip(w, c)]

    dp = [0] * (V + 1)

    for i in range(n):
        for j in range(V, -1, -1):
            if j + w[i] <= V:
                dp[j + w[i]] = max(dp[j + w[i]], dp[j] + c[i])

    print (dp[-1])
 

if __name__ == "__main__":
    for i in range(int(input())):
        function()