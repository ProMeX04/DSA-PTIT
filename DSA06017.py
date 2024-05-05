
def function(*arg, **kwarg):
    return sorted(arg[1] + arg[2])

if __name__ == "__main__":
    for i in range(int(input())):
        print(*function(input(), list(map(int,input().split())), list(map(int, input().split()))))

