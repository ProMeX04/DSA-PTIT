def Try(j, n):
    global res
    if n == 0:
        print("({})".format(" ".join(map(str,res[1:j]))), end = " ")
        return
    for i in range(min(res[j - 1], n), 0, -1):
        res[j] = i
        Try(j + 1, n - i)

def function():
    global res
    n = int(input())
    res = [0] * (n + 1)
    res[0] = n
    Try (1, n)
    print()



if __name__ == "__main__":
    for i in range(int(input())):
        function()