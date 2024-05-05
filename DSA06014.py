from math import sqrt

MAX = 1000000
A = (MAX + 1) * [1]
_ = 2
while _ * _ <= MAX:
    if A[_]:
        j = _ * _
        while j <= MAX:
            A[j] = 0
            j += _
    _ += 1

listPrime = []
for i in range(2, MAX + 1):
    if A[i]:
        listPrime.append(i)


def function(*arg, **kwarg):
    n = arg[0]
    ok = False
    for i in listPrime:
        if i >= n:
            break
        if A[n - i]:
            print(i, n - i, end="")
            ok = True
            break
    return "" if ok else -1


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input())))
