
def function(*arg, **kwarg):
    n, A = arg

    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if A[m] > A[j]:
             m = j
        A[m], A[i] = A[i], A[m] 
        print ("Buoc {0}:".format(i + 1), *A)
    return ""
if __name__ == "__main__":
    print(function(int(input()), list(map(int, input().split()))))
