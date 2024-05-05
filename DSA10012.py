from collections import defaultdict, deque

def bfs(adj, root):
    queue = deque([(root, 1)])
    res = defaultdict(int)
    res [root] = 1
    while queue:
        top, exp = queue.popleft()
        for i in adj[top]:
            if not res[i]:
                res[i]= exp + 1
                queue.append((i, exp + 1))
    return sum(res.values())



def function():
    v, e = map(int, input().split())

    adj = defaultdict(list)
    for i in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)

    s = 0
    v = len(adj)
    for i in adj:
        s += bfs(adj, i) - v

    print("{:.2f}".format(s / (v * (v - 1))))

if __name__ == "__main__":
    for i in range(int(input())):
        function()
