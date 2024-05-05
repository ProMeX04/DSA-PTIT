from collections import deque


def function(*line, **kwarg):
    n, m = line[0]
    A = [list(map(int, input().split())) for i in range(n)]
    B = [[0] * m for i in range(n)]
    myQueue = deque()
    myQueue.append((0, 0, 0))
    while len(myQueue):
        i, j, k = myQueue.popleft()

        if i + A[i][j] < n and B[i + A[i][j]][j] == 0:
            if i + A[i][j] == n - 1 and j == m - 1:
                return k + 1
            B[i + A[i][j]][j] = 1
            myQueue.append((i + A[i][j], j, k + 1))

        if j + A[i][j] < m and B[i][j + A[i][j]] == 0:
            if j + A[i][j] == m - 1 and i == n - 1:
                return k + 1
            B[i][j + A[i][j]] = 1
            myQueue.append((i, j + A[i][j], k + 1))
    return -1


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split())))
