
def function(*arg, **kwarg):
    A = arg[1]
    mi, ma = min(A), max(A)
    return ma - mi - len(set(A)) + 1


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input(), list(map(int, input().split()))))
