
def function():
    s = input()
    length = len (s)

    c_open = c_close = 0

    result = 0
    for i in range(length):
        if s[i] == ']':
            if c_open:
                c_open -= 1
            else:
                c_close += 1

        elif c_close:
            result += c_close
            c_close -= 1

        else:
            c_open += 1                
    print(result)


if __name__ == "__main__":
    for i in range(int(input())):
        function()