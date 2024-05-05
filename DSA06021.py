from bisect import bisect_left


def function(*arg, **kwarg):
    n, m = arg[0]
    A = arg[1]

    left, right = 0, n - 1
    result = 0
    mid = 1
    while A[left] < A[(left + 1) % n]:
        mid = (left + right + (mid == left)) // 2
        if A[mid] >= A[left]:
            left = mid
        else:
            right = mid

    if A[0] < m:
        return bisect_left(A[:left + 1], m) + 1
    else:
        return bisect_left(A[left + 1:], m) + left + 2


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(map(int, input().split()))))
