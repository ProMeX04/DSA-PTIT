from heapq import *

def dijkstra(matrix, n, m):
    pqueue = []
    heapify(pqueue)
    heappush(pqueue, (matrix[0][0], 0, 0))
    dp = [[99999999999] * m for i in range(n)]
    dp[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while True:
        w, i, j = heappop(pqueue)

        if i == n - 1 and j == m - 1:
            return dp[i][j]

        for _ in range(4):
            i_new = i + dx[_]
            j_new = j + dy[_]
            if 0 <= i_new < n and 0 <= j_new < m and w + matrix[i_new][j_new] < dp[i_new][j_new]:
                dp[i_new][j_new] = w + matrix[i_new][j_new]
                heappush(pqueue,(dp[i_new][j_new], i_new, j_new))


def function():
    ls = []
    while len(ls) < 2:
        ls += list(map(int, input().split()))
    n, m = ls
    matrix = [list(map(int, input().split())) for i in range(n)]
    print(dijkstra(matrix, n, m))


if __name__ == "__main__":
    for i in range(int(input())):
        function()
