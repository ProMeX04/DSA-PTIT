
def function(*line, **kwarg):
    n = line[0]
    A = [[] for i in range(n)]
    for i in range(n):
        A[i] = list(filter(lambda x: x > i, map(int, input().split())))

    for index, i in enumerate(A):
        for j in i:            
            print(index + 1, j)
    return ""


if __name__ == "__main__":
    function(int(input()))
