
def Try(j, n):
    global res, ans, count
    if n == 0:
        count += 1
        ans.append("({})".format(" ".join(map(str,res[1:j]))))
        return
    for i in range(min(res[j - 1], n), 0, -1):
        res[j] = i
        Try(j + 1, n - i)

def function():
    global res, count, ans
    count = 0
    ans = []
    n = int(input())
    res = [0] * (n + 1)
    res[0] = n
    Try (1, n)
    print(count)
    print(*ans)



if __name__ == "__main__":
    for i in range(int(input())):
        function()