
def function(*arg, **kwarg):
    return arg[1] * arg[2]
arr     

if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input(), max(list(map(int, input().split()))),
                       min(list(map(int, input().split())))))
