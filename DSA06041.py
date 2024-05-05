from collections import Counter


def function(*arg, **kwarg):
    dictt = Counter(arg[1])
    k = dictt.most_common(1)[0][0]
    return k if dictt[k] > arg[0]//2 else "NO"


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))
