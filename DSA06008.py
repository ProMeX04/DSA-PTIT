from bisect import bisect_left, bisect_right


def function(*arg, **kwarg):
    n, m = arg[0]
    A, B = sorted(arg[1]), sorted(arg[2])

    result = (n - bisect_left(A, 2)) * B.count(1) + A.count(3) * B.count(2) + B.count(0) * (n - bisect_left(A,1))
    for i in A:
        if i == 2:
            result += (m - bisect_left(B, 5))
        if i >= 3:
            result += (m - bisect_left(B, i + 1))
    return result


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(
            map(int, input().split())), list(map(int, input().split()))))
