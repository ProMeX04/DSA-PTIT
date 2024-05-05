
def function(*arg, **kwarg):
    n, A = arg

    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
        print ("Buoc {0}:".format(i + 1), *A)
    return ""
if __name__ == "__main__":
    print(function(int(input()), list(map(int, input().split()))))
