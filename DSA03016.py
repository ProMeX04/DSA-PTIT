
def function():
    s, n = map(int, input().split())
    if s == 0 and n > 1 or s > n * 9:
        print(-1)
        return


    num = [0] * n
    num[0] = 1
    s -= 1
    i = n - 1
    while s: 
        if s >= 9:
            num[i] += 9
            s -= 9
            i -= 1
        else:
            num[i] += s
            s = 0
    print("".join(map(str,num)))

if __name__ == "__main__":
    for i in range(int(input())):
        function()