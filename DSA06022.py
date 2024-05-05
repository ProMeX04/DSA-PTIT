def function(*arg, **kwarg):
    n, A = arg

    min1, min2 = 999999999999, 999999999999

    for i in A:
        if i < min1:
            min2 = min1
            min1 = i
        elif i < min2 and i > min1 :
            min2 = i
    if min2 == 999999999999 or min1 == min2:
        return (-1,)
    return min1, min2


if __name__ == "__main__":
    for i in range(int(input())):
        print(*function(int(input()), list(map(int, input().split()))))
