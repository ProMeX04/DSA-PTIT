import bisect


def function(*arg, **kwarg):
    n, m = arg[0]
    A = sorted(arg[1])
    count = 0
    for i in range(n):
        l = bisect.bisect_left(A[i + 1:], m - A[i]) + i + 1
        if l < n and A[l] == m - A[i]:
            r = bisect.bisect_right(A[i + 1:], m - A[i]) + i + 1
            count += r - l


    return count


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(map(int, input().split()))))
