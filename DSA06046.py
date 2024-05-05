
def function(*line, **kwarg):
    n, A = line
    A.sort()
    result = 1000000000000000
    for i in range(1, n):
        result = min(result, A[i] - A[i - 1])
    return result


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))

