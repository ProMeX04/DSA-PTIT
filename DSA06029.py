from bisect import bisect_left


def insertionSort(A: list, i: int, n: int, B: list) -> None:
    if i < n:
        pos = bisect_left(B, A[i])
        B.insert(pos, A[i])
        insertionSort(A, i + 1, n, B[:])
        print(f"Buoc {i}:",*B)


def function(*arg, **kwarg):
    n, A = arg
    insertionSort(A.copy(), 0, n, [])
    return ""


if __name__ == "__main__":
    print(function(int(input()), list(map(int, input().split()))))
