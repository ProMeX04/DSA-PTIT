
def function(*line, **kwarg):
    n, A = line
    L = [0] * (n + 1)
    for i in A:
        L[i] = L[i - 1] + 1 if L[i - 1] else 1

    print(L)
    return n - max(L)


if __name__ == "__main__":
    print(function(int(input()), list(map(int, input().split()))))
