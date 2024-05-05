def function(*arg, **kwarg):
    n, A = arg
    A = list(zip(A, range(n)))
    A.sort(key=lambda x: (x[0], - x[1]))
    res = -1
    last = A[0][1]
    for i in range(1, n):
        res = max(res, A[i][1] - last)
        last = min(last , A[i][1])
    return -1 if res == 0 else res


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))
