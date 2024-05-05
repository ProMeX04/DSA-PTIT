from collections import deque, defaultdict


def check_cycle(adj, visited, u, found, parent):
    visited[u] = True
    for x in adj[u]:
        if not visited[x]:
            check_cycle(adj, visited, x, found, u)
        elif x != parent:
            found[0] = True


def function():
    v, e = map(int, input().split())
    ls = list(map(int, input().split()))
    adj = defaultdict(list)
    for i in range(0, 2 * v, 2):
        adj[ls[i]].append(ls[i + 1])
        adj[ls[i + 1]].append(ls[i])

    visited = defaultdict(bool)
    found = [False]
    for x in list(adj):
        if not visited[x]:
            check_cycle(adj, visited, x, found, -1)
            if found[0]:
                break
    print("YES" if found[0] else "NO")


if __name__ == "__main__":
    for i in range(int(input())):
        function()
