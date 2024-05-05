
def function(*line, **kwarg):
    string = line[0].split()
    print (*string[::-1], end = '')
    return ""
if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input()))

