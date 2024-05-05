from collections import defaultdict


def function():
    v, e = map(int, input().split())
    ls = []
    while len(ls) < 2 * e:
        ls += list(map(int, input().split()))

    adj = defaultdict(list)
    for i in range(e):
        adj[ls[2*i]] .append(ls[2*i + 1])
        adj[ls[2*i + 1]] .append(ls[2*i])

    visited = defaultdict(bool)

    def hamilton(l, i):        
        if l == v:
            return 1

        else:
            for x in adj[i]:
                if not visited[x]:
                    visited[i] = True
                    if hamilton(l + 1, x):
                        return 1
                    visited[i] = False
        return 0

    visited[1] = True
    if hamilton(1, 1):
        return 1
    return 0

if __name__ == "__main__":
    for i in range(int(input())):
        print(function())
