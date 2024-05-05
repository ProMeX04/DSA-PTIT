from collections import defaultdict, deque


def function():
    v, e = map(int, input().split())
    ls = []
    while len(ls) < 2 * e:
        ls += list(map(int, input().split()))

    adj = defaultdict(list)
    for i in range(e):
        adj[ls[2 * i]].append(ls[2 * i + 1])
        adj[ls[2 * i + 1]].append(ls[2 * i])

    for i,key in adj.items():
        key.sort()
    def cycle():
        visited = defaultdict(bool)
        stack = deque()
        stack.append(1)
        visited[1] = True
        par = defaultdict(int)
        while stack:
            u = stack.pop()
            for i in adj[u]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(u)
                    stack.append(i)
                    par[i] = u
                    break
                elif i == 1 and par[u] != i:
                    print(*stack, u, 1)
                    return
        print("NO")
    cycle()


if __name__ == "__main__":
    for i in range(int(input())):
        function()
