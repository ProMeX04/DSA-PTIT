from collections import deque
def bfs(begin):
    global adj, visited
    myQueue = deque()
    myQueue.append(begin)
    visited[begin] = True
    while len(myQueue):
        get = myQueue[0]
        myQueue.popleft()
        print (get, end = " ")
        for i in adj[get]:
            if not visited[i]:
                myQueue.append(i)
                visited[i] = True


def function():
    n, m, b = map(int, input().split())
    list_edges = list(map(int, input().split()))

    global adj, visited
    visited = [0] * (n + 1) 
    adj = [[]for i in range(n + 1)]
    k = 0
    for i in range(m):
        u, v = list_edges[k:k + 2]
        adj[u].append(v)
        k += 2

    bfs(b)
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        function()
