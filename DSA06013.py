
def function(*arg, **kwarg):
    n, m = arg[0]
    A = arg[1]

    return A.count(m) if A.count(m) != 0 else -1

if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(map(int, input().split()))))

