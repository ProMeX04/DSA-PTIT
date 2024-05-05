def selectionSort(A: list, i: int, n: int) -> None:
    if i < n - 1:
        k = i
        for j in range(i + 1, n):
            if A[k] > A[j]:
                k = j
        A[i], A[k] = A[k], A[i]
        selectionSort(A.copy(), i + 1, n)
        print(f"Buoc {i + 1}:", *A)
        return


def function(*arg, **kwarg):
    n, A = arg
    selectionSort(A.copy(), 0, n)
    return ""


if __name__ == "__main__":
    print(function(int(input()), list(map(int, input().split()))))
