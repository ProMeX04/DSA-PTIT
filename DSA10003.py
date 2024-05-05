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

def function():
    v, e = map(int, input().split())

    ls = list(map(int, input().split()))
    djs = DisjointSet(v)
    cycle = False
    for i in range(0, 2 * v, 2):
        if djs.find(ls[i]) != djs.find(ls[i + 1]):
            djs.union(ls[i], ls[i + 1])
        else:
            cycle = True

    print("YES" if cycle else "NO")
if __name__ == "__main__":
    for i in range(int(input())):
        function()