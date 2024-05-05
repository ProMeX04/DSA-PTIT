
def function(*arg, **kwarg):
    n, A = arg[0], arg[1]
    for i in range(3):
        for x in range(A.count(i)):
            print(i, end = " ")
    return " "
if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))
