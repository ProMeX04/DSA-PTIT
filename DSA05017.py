
def function():
    n = int(input())
    ls = list(map(int, input().split()))
    dp1 = [0] * n
    for i in range(n):
        dp1[i] = ls[i]
        for j in range(i):
            if ls[i] > ls[j]:
                dp1[i] = max(dp1[i], dp1[j] + ls[i])

    dp2 = [0] * n
    for i in range(n - 1, -1, -1):
        dp2[i] = ls[i]
        for j in range(n - 1, i, -1):
            if ls[i] > ls[j]:
                dp2[i] = max(dp2[i], dp2[j] + ls[i])

    result = 0
    for i in range(n):
        for j in range(n - 1, i - 1, -1):
            if ls[j] != ls[i]:
                result = max(result, dp1[i] + dp2[j])
            else:
                result = max(result, dp1[i] + dp2[j] - ls[i])        

    print(result)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
