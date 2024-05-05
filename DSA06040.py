from collections import Counter


def function(*line, **kwarg):
    n, m, p = line[0]
    A, B, C = map(Counter, line[1:])
    result = A & B & C
    for i, j in result.items():
        print((str(i) + " ") * j, end="")
    return "" if len(result) != 0 else -1


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(map(int, input().split())), list(
            map(int, input().split())), list(map(int, input().split()))))
