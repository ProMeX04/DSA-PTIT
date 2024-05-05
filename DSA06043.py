
def function(*line, **kwarg):
    n, A = line
    total = sum(A)
    k = 0
    if total % 2 == 1:
        return -1

    for i in range(n):
        if 2 * k == (total - A[i]):
            return i + 1
        k += A[i]
    return -1


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))
