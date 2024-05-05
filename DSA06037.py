
def function():
    n = int(input())
    ls = list(map(int, input().split()))
    new_ls = []
    for index,i in enumerate(ls):
        new_ls.append((i, index + 1))

    new_ls.sort()
    res = []
    MAX = 0
    for index,val in enumerate(new_ls,start = 1):
        MAX = max(MAX, val[1])
        if index >= MAX:
            res.append(MAX)
    print(len(res) - 1)
    print(*res[:-1])

if __name__ == "__main__":
    for i in range(int(input())):
        function()