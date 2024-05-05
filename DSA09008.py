from collections import deque



def function():
    v, e = map(int, input().split())

    adj = [[] for i in range(10000)]
    ls = list(map(int, input().split()))

    for i in range(0, 2 * e, 2):
        adj[ls[i]].append(ls[i + 1])
        adj[ls[i + 1]].append(ls[i])
    visited = [0] * 100000
    def bfs(u):
        visited[u] = True
        queue = deque()
        queue.append(u)
        while queue:
            front = queue.popleft()
            for i in adj[front]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
    count = 0
    for i in range(1, v):
        if not visited[i]:
            bfs(i)
            count += 1    
    print(count)

if __name__ == "__main__":
    for i in range(int(input())):
        function()