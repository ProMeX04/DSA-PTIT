
def function (): 
    n, m = map(int , input().split())
    ls = [list(input()) for i in range(n)]

    def check(x, y):
        return x < n and y < m and x >= 0 and y >= 0 and ls[x][y] == "W"

    def find(x, y):
        ls[x][y] = '.'
        for i in range(-1, 2):
            for j in range(-1, 2):
                if check (x + i,y + j):
                    find(x + i, y + j)

    count = 0
    for i in range(n):
        for j in range(m):
            if ls[i][j] == "W": 
                find(i, j)
                count += 1

    print(count)

if __name__ == "__main__":
    function()