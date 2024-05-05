from collections import defaultdict


def function():
    v, e = map(int, input().split())

    ls = []
    while len(ls) < 2 * e:
        ls += list(map(int, input().split()))

    adj = defaultdict(list)

    for i in range(e):
        adj[ls[2*i]].append(ls[2*i + 1])
        adj[ls[2*i + 1]].append(ls[2*i])

    low = defaultdict(list)
    num = defaultdict(list)
    par = defaultdict(int)

    time = 1
    list_articulation_points = []

    def tarjan(u):
        nonlocal time
        low[u] = num[u] = time
        time += 1
        child = 0
        for v in adj[u]:
            if not num[v]:
                par[v] = u
                tarjan(v)
                child += 1
                low[u] = min(low[u], low[v])
                if par[u] and low[v] >= num[u]:
                    list_articulation_points.append(u)
            else:
                low[u] = min(low[u], num[v])
        if not par[u] and child > 1:
            list_articulation_points.append(u)

    for i in adj:
        if not par[i]:
            tarjan(i)
    print(*sorted(list_articulation_points))


if __name__ == "__main__":
    for i in range(int(input())):
        function()
