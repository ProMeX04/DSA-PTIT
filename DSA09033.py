
from collections import defaultdict, deque
from math import comb


def function():
    v, e = map(int, input().split())
    adj = defaultdict(list)

    for i in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    visited = defaultdict(bool)

    def dfs(u):
        stack = deque([u])
        count = 1
        visited[u] = True
        while stack:
            top = stack.pop()
            for i in adj[top]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(top)
                    stack.append(i)
                    count += 1
                    break
        return count

    need_edges = 0
    for i in adj:
        if not visited[i]:
            need_edges += comb(dfs(i), 2)

    print("YES" if need_edges == e else "NO")

if __name__ == "__main__":
    for i in range(int(input())):
        function()
