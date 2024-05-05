
def Try(j, vCur, posCur):
    global n, listVal, fopt, minVal, visited
    visited[posCur] = True
    if j == n - 1:
        fopt = vCur
    else:
        for i in range(n):
            vNex = vCur + listVal[posCur][i]
            if not visited[i] and vNex + (n - j - 1) * minVal < fopt:
                Try(j + 1, vNex, i)
    visited[posCur] = False


def function():
    global n, listVal, fopt, minVal, visited
    minVal = 9999999999
    fopt = 9999999999
    n = int(input())
    visited = [0] * n
    listVal = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                minVal = min(minVal, listVal[i][j])
    for i in range(n):
        Try(0, 0, i)
    print(fopt)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
