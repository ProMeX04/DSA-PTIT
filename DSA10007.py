from collections import defaultdict, deque
def function():
    v, e, bv = map(int, input().split())
    adj = defaultdict(list)

    for i in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    visited = defaultdict(bool)
    def bfs(bv):
        queue = deque()
        queue.append(bv)
        visited[bv] = True
        Tree = []
        while queue:
            u = queue.popleft()
            for i in adj[u]:
                if not visited[i]:
                    Tree.append((u, i))
                    visited[i] = True
                    queue.append(i)

        if len(Tree) == v - 1:
            for i in Tree:
                print(*i)
        else:print(-1)
    bfs(bv)
if __name__ == "__main__":
    for i in range(int(input())):
        function()