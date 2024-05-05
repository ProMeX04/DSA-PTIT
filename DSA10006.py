from collections import defaultdict,deque
def function():
    v,e,bv = map(int, input().split())

    adj = defaultdict(list)
    for i in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    visited = [0] * (v + 1)
    def dfs(u):
        stack = deque()
        stack.append(u)
        visited[u] = True
        dfs_tree = []
        while stack:
            top = stack.pop()
            for i in adj[top]:
                if not visited[i]:
                    dfs_tree.append((top, i))
                    visited[i] = True
                    stack.append(top)
                    stack.append(i)
                    break
        if visited.count(1) == v:
            for i in dfs_tree:
                print(*i)
        else:
            print(-1)
    dfs(bv)

if __name__ == "__main__":
    for i in range(int(input())):
        function()