
def function():
    n = input()
    result = n[0]
    for i in range(1,len(n)):
        result += str(int(n[i]) ^ int(n[i - 1]))
    print(result)


if __name__ == "__main__":
    for i in range(int(input())):
        function()