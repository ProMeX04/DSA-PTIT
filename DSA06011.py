
def function(*arg, **kwarg):
    n, A = arg

    result = 99999999999
    for i in range(n):
        for j in range(i + 1, n):
            if abs(result) > abs(A[i] + A[j]):
                result = A[i] + A[j]
    return result


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))
