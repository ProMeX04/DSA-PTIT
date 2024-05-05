
def function(*arg, **kwarg):
    ok = True
    k = 1
    while ok:
        ok = False
        for i in range(1, arg[0]):
            if arg[1][i - 1] > arg[1][i]:
                arg[1][i], arg[1][i-1] = arg[1][i-1], arg[1][i]
                ok = True
        if ok:
            print (f"Buoc {k}:", *arg[1])
        k += 1
    return ""


if __name__ == "__main__":
    print(function(int(input()), list(map(int, input().split()))))
