def function(*line, **kwarg):
    n = line[0]
    A = [8] * (n)
    l = n
    while l:
        for i in range(l):
            print(A[i], end="")
        print(end=" ")
        j = l - 1
        while A[j] == 6:
            A[j] = 8
            j -= 1
        if j == -1:
            l -= 1
        else:
            A[j] = 6

    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input())))
