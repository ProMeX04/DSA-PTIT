from collections import defaultdict


def function():
    v, e = map(int, input().split())
    minDist = [(v + 1) * [100000] for i in range(v + 1)]
    for i in range(e):
        x, y, w = map(int, input().split())
        minDist[x][y] = minDist[y][x] = w
    for i in range(1, v + 1):
        minDist[i][i] = 0

    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                minDist[i][j] = min(
                    minDist[i][j], minDist[i][k] + minDist[k][j])

    q = int(input())
    for i in range(q):
        u, v = map(int, input().split())
        print(minDist[u][v])


if __name__ == "__main__":
    function()
