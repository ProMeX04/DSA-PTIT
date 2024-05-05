
def function():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(n)]

    dx = [1,1,1,-1,-1,-1,0,0]
    dy = [0,-1,1,-1,0,1,1,-1]

    def check(idx, jdy):
        return idx < n and jdy < m and idx >= 0 and jdy >= 0 and matrix[idx][jdy]

    def island(i, j):
        matrix[i][j] = 0
        for _ in range(8):
            idx = i + dx[_]
            jdy = j + dy[_]
            if check(idx, jdy):
                island(idx, jdy)

    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                island(i,j)
                count += 1
    print(count) 


if __name__ == "__main__":
    for i in range(int(input())):
        function()