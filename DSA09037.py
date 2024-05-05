from collections import defaultdict, deque
from multiprocessing import Pool


def dfs(x):
    u, adj = x[0], x[1]
    visited = defaultdict(bool)
    stack = deque([u])
    visited[u] = True
    while stack:
        top = stack.pop()
        for i in adj[top]:
            if not visited[i]:
                visited[i] = True
                stack.append(top)
                stack.append(i)
                break
    return set(visited.keys())


def function():
    k, n, m = map(int, input().split())

    ls = []
    for i in range(k):
        ls.append(int(input()))

    adj = defaultdict(list)
    for i in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)

    with Pool() as pool:
        res = pool.map(dfs, [(ls[i], adj) for i in range(k)])

    print(len(set.intersection(*res)))


if __name__ == "__main__":
    function()
