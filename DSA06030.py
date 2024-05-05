from bisect import bisect_left


def bubbleSort(A: list, j, n: int, ok: bool) -> None:
    if ok:
        ok = False
        for i in range(1, n):
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]
                ok = True
        bubbleSort(A[:], j + 1, n, ok)
        if ok:
            print(f"Buoc {j}:", *A)


def function(*arg, **kwarg):
    n, A = arg
    bubbleSort(A.copy(), 1, n, 1)
    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))
