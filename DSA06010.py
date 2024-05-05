
def function(*arg, **kwarg):
    A = arg[1]
    return sorted(A)

if __name__ == "__main__":
    for i in range(int(input())):
        print(*function(int(input()), set(filter(
            lambda x: x.isdigit(), list(input())))))
