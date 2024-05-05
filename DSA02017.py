
def Try (i, current):
    global chessboard, result, col, first_diagonal, secondary_diagonal
    if i == 8:
        result = max (result, current)
    else:
        for j in range (8):
            if not col[j] and not first_diagonal[7 - i + j] and not secondary_diagonal[i + j]:
                col[j] = first_diagonal[7 - i + j] = secondary_diagonal[i + j] = True
                Try(i + 1, current + chessboard[i][j])
                col[j] = first_diagonal[7 - i + j] = secondary_diagonal[i + j] = False

def function():
    global chessboard, result, col, first_diagonal, secondary_diagonal
    result = 0
    first_diagonal = [False] * 20
    secondary_diagonal = [False] * 20
    col = [False] * 8
    chessboard = [list(map(int, input().split())) for i in range (8)]
    Try(0, 0)
    print (result)

if __name__ == "__main__":
    for i in range(int(input())):
        function()