from collections import defaultdict


def function(*arg, **kwarg):
    n, A = arg

    myDict = defaultdict(int)

    for i in A:
        myDict[i] += 1

    for a, b in sorted(myDict.items(), key=lambda x: (x[1], -x[0]), reverse=True):
        print ((str(a) + " ") * b, end = "")
    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))
