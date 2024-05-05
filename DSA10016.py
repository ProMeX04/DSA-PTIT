from math import sqrt
from collections import defaultdict


class DisjointSet:
    def __init__(self, n = 0):
        self.n = n
        self.rank = [0] * (self.n + 1)
        self.parent = [i for i in range(n + 1)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

    def print(self):
        print(self.parent)

def distance(A, B):
    return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


def function():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(float, input().split())))

    list_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            list_edges.append((distance(points[i - 1], points[j - 1]), i, j))

    list_edges.sort()


    def kruskal():
        djs = DisjointSet(n)
        total = 0
        for w, u, v in list_edges:
            if djs.find(u) != djs.find(v):
                total += w
                djs.union(u,v)
        return total
    print("{:.6f}".format(kruskal()))


if __name__ == "__main__":
    for i in range(int(input())):
        function()
