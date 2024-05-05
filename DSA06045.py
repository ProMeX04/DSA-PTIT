
def function():
    n = int(input())
    s = list(input())
    result = 0
    count = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
            result += i - (count <= i)
        else:
            result += i - count
            count = 1
    print(result)


if __name__ == "__main__":
    function()
