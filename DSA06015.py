# merge sort

def merge(A, l, mid, r):
    i = j = 0
    left = A[l:mid + 1]
    right = A[mid + 1:r + 1]

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[l + i + j] = left[i]
            i += 1
        else:
            A[l + i + j] = right[j]
            j += 1

    while i < len(left):
        A[l + i + j] = left[i]
        i += 1

    while j < len(right):
        A[l + i + j] = right[j]
        j += 1


def mergeSort(A, l, r):
    if l < r:
        mid = (l + r) // 2
        mergeSort(A, l, mid)
        mergeSort(A, mid + 1, r)
        merge(A, l, mid, r)


def function(*arg, **kwarg):
    n, A = arg[0], arg[1]
    mergeSort(A, 0, n - 1)
    return A


if __name__ == "__main__":
    for i in range(int(input())):
        print(*function(int(input()), list(map(int, input().split()))))
