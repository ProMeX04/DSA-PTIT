from itertools import combinations


def Try(j, cur, total):
    global result, n, ls, dp, visited
    if j == n:
        result = min(result, total)
    elif total < result:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                Try(j + 1, i, total + (dp[cur][i] if j > 0 else 0))
                visited[i] = False


def function():
    global result, visited, dp, n
    result = 99999999
    n = int(input())
    ls = [set(input()) for i in range(n)]
    dp = [[0] * n for i in range(n)]
    visited = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = dp[j][i] = len(ls[i] & ls[j])

    Try(0, 0, 0)
    print(result)


if __name__ == "__main__":
    function()
