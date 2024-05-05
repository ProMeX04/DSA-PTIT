from collections import defaultdict, deque

def function():
    v, e = map(int, input().split())
    adj = defaultdict(list)

    for i in range(e):
        x, y = map(int ,input().split())
        adj[x].append(y)
        adj[y].append(x)


    visited = defaultdict(bool)
    def dfs(u: int):
        count = 1
        stack = deque()
        stack.append(u)
        visited[u] = True

        while stack:
            top = stack.pop()
            for i in adj[top]:
                if not visited[i]:
                    visited[i] = True
                    count += 1
                    stack.append(top)
                    stack.append(i)
                    break
        return count
    res = 0
    for i in adj:
        if not visited[i]:
            res = max(res, dfs(i))

    print(res)
if __name__ == "__main__":
    for i in range(int(input())):
        function()