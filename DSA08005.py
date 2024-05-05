def function(*line, **kwarg):
    n = line[0]
    A = [0] * 100
    l = 100
    for i in range(n):
        j = 99
        while A[j] == 1:
            A[j] = 0
            j -= 1
        A[j] = 1
        l = min(j, l)
        for k in range(l, 100, 1):
            print(A[k], end="")
        print (" ", end = "")

    return ""

if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input())))

