from collections import deque



def function():
    v, e, a, b = map(int, input().split())

    adj = [[] for i in range(v + 1)]
    ls = list(map(int, input().split()))

    for i in range(0, 2 * e, 2):
        adj[ls[i]].append(ls[i + 1])
        adj[ls[i + 1]].append(ls[i])

    


    def bfs():
        visited = [0] * (v + 1)
        visited[a] = True
        queue = deque()
        queue.append(a)
        found = False
        parent = [i for i in range(v + 1)]
        while queue and not found:
            front = queue.popleft()
            for i in adj[front]:
                if not visited[i]:
                    parent[i] = front
                    visited[i] = True
                    queue.append(i)
                    if i == b:
                        found = True

        if found:
            temp = b
            res = []
            while temp != parent[temp]:
                res.append(temp)
                temp = parent[temp]
            print(a, *res[::-1])
        else:
            print(-1)
    bfs()


if __name__ == "__main__":
    for i in range(int(input())):
        function()