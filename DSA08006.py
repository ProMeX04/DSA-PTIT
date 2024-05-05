def function(*line, **kwarg):
    n = line[0]
    A = [0] * 100
    l = 100
    number = "9"
    while int(number) % n != 0:
        number = ""
        j = 99
        while A[j] == 1:
            A[j] = 0
            j -= 1
        A[j] = 1
        l = min(j, l)
        for k in range(l, 100, 1):
            number += ("9" if A[k] else "0")
    return number

if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input())))

