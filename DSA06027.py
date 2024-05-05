def interchangeSort(A: list, i: int, n: int) -> None:
    if i < n - 1:
        for j in range(i + 1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
        interchangeSort(A.copy(), i + 1, n)
        print(f"Buoc {i + 1}:",*A)
        return


def function(*arg, **kwarg):
    n, A = arg
    interchangeSort(A.copy(), 0, n)
    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))
