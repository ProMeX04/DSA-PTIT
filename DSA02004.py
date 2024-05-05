
def function(*arg, **kwarg):
    n = arg[0]
    arr = [list(map(int, input().split())) for i in range(n)]
    # print (arr[n - 1][n - 1])
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    listWay = list(zip(dx, dy))

    char = {(1, 0): "D", (0, -1): "L", (0, 1): "R", (-1, 0): "U"}

    ok = False

    def moveInMatrix(i, j, way):
        if i == n - 1 and j == n - 1:
            print(way, end=" ")
            nonlocal ok
            ok = True
        else:
            arr[0][0] = 0
            for _ in listWay:
                idx = i + _[0]
                jdx = j + _[1]
                if idx >= 0 and jdx >= 0 and idx < n and jdx < n and arr[idx][jdx] == 1:
                    arr[idx][jdx] = 0
                    moveInMatrix(idx, jdx, way + char[_])
                    arr[idx][jdx] = 1

    if arr[0][0] == 1:
        moveInMatrix(0, 0, "")
    return (-1 if not ok else "")


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input())))
