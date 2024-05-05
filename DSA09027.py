def dfs(begin):
    global adj, visited, parent, top
    visited[begin] = True
    parent[begin] = top
    for i in adj[begin]:
        if not visited[i]:
            dfs(i)


def function():
    n, m = map(int, input().split())
    global adj, visited, parent, top
    adj = [[] for i in range(n + 1)]
    visited = [0] * (n + 1)
    parent = [0] * (n + 1)
    for i in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, n + 1):
        if not visited[i]:
            top = i
            dfs(top)

    q = int(input())
    for i in range(q):
        u, v = map(int, input().split())
        if parent[u] == parent[v]:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    for i in range(int(input())):
        function()
