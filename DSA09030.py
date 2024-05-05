from collections import defaultdict,deque
def function():
    v, e = map(int, input().split())
    adj = defaultdict(list)

    for i in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)


    queue = deque()

    setV = defaultdict(int)

    for i in adj:
        if not setV[i]:
            queue.append(i)
            setV[i] = 1
            while queue:
                top = queue.popleft()
                for j in adj[top]:
                    if setV[j] == setV[top]:
                        print("NO")
                        return
                    if not setV[j]:
                        setV[j] = 3 - setV[top]
                        queue.append(j)
    print("YES")

if __name__ == "__main__":
    for i in range(int(input())):
        function()

