

def Try(Total, result, posmin):
    global size, total, ls
    if Total == 0:
        ans.append(result.rstrip() +"}")

    elif Total > 0:
        for i in range(posmin, size):
            Try(Total - ls[i], result + str(ls[i]) + " ", i)

def function():
    global size, total, ans, ls
    ans = []
    size, total = map (int, input().split())
    ls = list(map(int, input().split()))
    Try (total, "{", 0)
    if len(ans) > 0:
        print (len(ans), *ans) 
        
    else:
        print(-1    )

if __name__ == "__main__":
    for i in range(int(input())):
        function()