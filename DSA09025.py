def dfs(begin):
    global e, adj, visited, found, way
    way.append(begin)
    visited[begin] = True
    if begin == e:
        found = True
        print (*way)
    else:
        for i in adj[begin]:
            if not visited[i] and not found:
                dfs(i)
    way.pop()



def function():
    global e, adj, visited, found, way
    n, m, b, e = map(int, input().split())
    found = False

    way = []
    visited = [0] * (n + 1)
    list_edges = list(map(int, input().split()))
    adj = [[] for i in range(n + 1)]
    k = 0
    for i in range(m):
        u, v= list_edges[k: k + 2]
        adj[u].append(v)
        k += 2

    dfs(b)
    if not found:
        print (-1)


if __name__ == "__main__":
    for i in range(int(input())):
        function()