
def function():
    n, m = map(int, input().split())
    matrix = [list(input()) for i in range(n)]

    iS = jS = iT = jT = None

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'S':
                iS, jS = i, j
            elif matrix[i][j] == 'T':
                iT, jT = i, j

    direct = {"U": (-1, 0),
              "D": (1, 0),
              "R": (0, 1),
              "L": (0, -1)
              }

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    direct = ["U", "D", "L", "R"]

    def check(i, j):
        return i >= 0 and j >= 0 and i < n and j < m and (matrix[i][j] == '.' or matrix[i][j] == "T") 

    def move(i=iS, j=jS, prev_direct=None, num_change=-1):
        if num_change > 2:
            return

        if i == iT and j == jT:
            return True

        else:
            for _ in range(4):
                if check(i + dx[_], j + dy[_]):
                    matrix[i][j] = "*"
                    if (move(i + dx[_], j + dy[_], direct[_],
                             num_change + (prev_direct != direct[_]))) == True:
                        return True
    if move():print("YES")
    else: print("NO")


if __name__ == "__main__":
    for i in range(int(input())):
        function()