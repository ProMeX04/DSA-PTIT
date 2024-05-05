
def function(*arg, **kwarg):
    return sorted(arg[1],reverse = True)[:list(arg[0])[1]]

if __name__ == "__main__":
    for i in range(int(input())):
        print(*function(map(int, input().split()), list(map(int, input().split()))))

