from collections import Counter
def function(*arg, **kwarg):
    n, k = arg[0]
    myDict = Counter(arg[1])

    result = 0
    for i in myDict.items():
        if (k - i[0] > i[0]):
            result += i[1] * myDict[k - i[0]]
        elif k == 2 * i[0]:
            result += i[1] * (i[1] - 1) // 2

    return result


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(map(int, input().split()))))
