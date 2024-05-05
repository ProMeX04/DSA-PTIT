class DisjointSet:
    def __init__(self, n=0):
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1

from collections import defaultdict
def function():
    v, e = map(int, input().split())

    edges = [list(map(int, input().split())) for i in range(e)]

    edges.sort(key = lambda x: x[2])

    djs = DisjointSet(v)
    res = 0
    for i in edges:
        if djs.find(i[0]) != djs.find(i[1]):
            djs.union(i[0], i[1])
            res += i[2]

    print(res)
if __name__ == "__main__":
    for i in range(int(input())):
        function()