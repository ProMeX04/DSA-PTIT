
def dfs(begin):
    global adj, visited
    print (begin, end = " ")
    visited[begin] = True
    for i in adj[begin]:
        if not visited[i]:
            dfs(i)

def function():
    n, m, b = map(int, input().split())
    list_edges = list(map(int, input().split()))

    global adj, visited
    visited = [0] * (n + 1) 
    adj = [[]for i in range(n + 1)]
    k = 0
    for i in range(m):
        u, v = list_edges[k:k + 2]
        adj[u].append(v)
        k += 2

    dfs(b)
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        function()
