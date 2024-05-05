from bisect import bisect_right


def function():
    n = int(input())
    ls = list(map(int, input().split()))

    dp1 = [1]
    dp2 = [1]

    count = 0
    for i in range(1, n):
        if ls[i] > ls[i - 1]:
            dp1.append(dp1[-1] + 1)
        else:
            dp1.append(1)
    ls = ls[::-1]

    for i in range(1, n):
        if ls[i] > ls[i - 1]:
            dp2.append(dp2[-1] + 1)
        else:
            dp2.append(1)
    dp2.reverse()

    # print(dp1, dp2)
    result = 0
    for i in range(n - 1):
        result = max(result, dp1[i] + dp2[i] - 1)
    result = max(result, dp1[-1], dp2[0])
    print(result)

if __name__ == "__main__":
    for i in range(int(input())):
        function()
