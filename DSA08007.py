
def function(*line, **kwarg):
    string = line[0]

    result = 0
    l = len(string)
    x = 1
    for index, i in enumerate(string, start=1):

        if i > "1":
            result += 2**(l - index + 1)
            x = 0
            break
        elif i == "1":
            result += 2**(l - index)
    return result + x - 1


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input()))
