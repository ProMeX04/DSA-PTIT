from itertools import combinations
def function():
    n, k, m = map(int, input().split())

    matrix = [[0] * (2 * n - 1) for i in range(2 * n - 1)]

    for i in range(m):
        u, v, x, y = map(lambda x: 2 * (int(x) - 1), input().split())
        if u == x:
            matrix[u][(v + y) // 2] = "|"
        else:
            matrix[(x + u) // 2][y] = "-"

    for i in range(k):
        ls = [] 
        while not ls:
            ls = list(map(lambda x: int(x) - 1, input().split()))
        matrix[2 * ls[0]][2 * ls[1]] = 2
    
    dx = [0, 0, -2, 2]
    dy = [2, -2, 0, 0]

    ls = []
    cnt = 1

    # for i in matrix:
    #     for j in i:
    #         print("{:}".format(j if j != -1 else "T"), end = " ")
    #     print()
    def check(i, j):
        return 0 <= i < 2 * n - 1 and 0 <= j < 2 * n - 1

    def move(i, j):
        nonlocal cnt
        matrix[i][j] = -1
        for _ in range(4):
            iNew = i + dx[_]
            jNew = j + dy[_]
            if check(iNew, jNew) and matrix[i + dx[_] // 2][j + dy[_] // 2] == 0:
                if matrix[iNew][jNew] == 2:
                    cnt += 1
                if matrix[iNew][jNew] >= 0:
                    move(iNew, jNew)


    for i in range(0, 2 * n - 1, 2):
        for j in range(2 * n - 1):
            if matrix[i][j] == 2:
                move(i, j)
                ls.append(cnt)
                cnt = 1
    res = 0
    for i in combinations(ls, 2):
        res += i[0] * i[1]
    print(res)


if __name__ == "__main__":
    function()
