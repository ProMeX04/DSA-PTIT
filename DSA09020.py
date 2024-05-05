
def function(*line, **kwarg):
    n = line[0]
    adjacency_matrix = [[0]*n for i in range(n)]
    for i in range(n):
        arr = list(map(int, input().split()))
        for x in arr:
            adjacency_matrix[i][x - 1] = 1
            adjacency_matrix[x - 1][i] = 1
        print (*adjacency_matrix[i])
if __name__ == "__main__":
    function(int(input()))
