from bisect import bisect_left
def function(*arg, **kwarg):
    n, m = arg[0]
    A = arg[1]

    k = bisect_left(A, m)
    if k < n and A[k] == m:
        return 1
    else: return -1


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(map(int, input().split()))))

