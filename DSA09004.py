from collections import deque

visited = [False] * 100000
adj = [[] for i in range(100000 + 1)]


def dfs(s):
    visited[s] = True
    print(s, end=" ")
    for i in adj[s]:
        if not visited[i]:
            dfs(i)


def function(*line, **kwarg):
    v, e, s = line[0]

    for i in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    for i in range(1, v + 1):
        adj[i].sort()
    dfs(s)
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        function(map(int, input().split()))
