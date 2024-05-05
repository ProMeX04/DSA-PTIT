def combine (j, minn, s, k, n):
    global cnt 
    if j == k:
        if s == 0:
            cnt += 1
    else:
        for i in range(minn, n + 1):
            combine(j + 1, i + 1, s - i, k, n)



def function(n, k ,s):
    global cnt
    cnt = 0
    combine(0, 1, s, k, n)
    print (cnt)

if __name__ == "__main__":
    while True:
        n, k, s = map(int, input().split())
        if n or k or s:
            function(n, k ,s)
        else:
            break
