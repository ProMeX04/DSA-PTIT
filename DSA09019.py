from collections import defaultdict
def function():
    v, e = map(int, input().split())
    ls = []
    while len(ls) < 2 * e:
        ls += list(map(int, input().split()))

    adj = defaultdict(list)
    for i in range(e):
        adj[ls[2 * i]].append(ls[2 * i + 1])
        adj[ls[2 * i + 1]].append(ls[2 * i])

    visited = defaultdict(bool)
    def dfs(b_vertex, par):
        visited[b_vertex] = True
        for x in adj[b_vertex]:
            if not visited[x]:
                if dfs(x, b_vertex):
                    return True
            elif x != par:
                return True
        return False

    for i in range(1, v + 1):
        if not visited[i]:
            if dfs(i, 0):
                return "YES"
    return "NO"
if __name__ == "__main__":
    for i in range(int(input())):
        print(function())