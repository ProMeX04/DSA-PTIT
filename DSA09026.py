from collections import deque


def bfs(begin):
    global e, adj, visited, found, parrent
    myQueue = deque()
    myQueue.append(begin)
    visited[begin] = True
    parrent = {}
    parrent[begin] = begin
    way = []

    while len(myQueue):
        front = myQueue.popleft()
        for i in adj[front]:
            if not visited[i]:
                visited[i] = True
                myQueue.append(i)
                parrent[i] = front
            if i == e:
                way.append(i)
                k = i
                while k != parrent[k]:
                    k = parrent[k]
                    way.append(k)

                print (*way[::-1])
                return
    print (-1)
def function():
    global e, adj, visited, found, parrent
    n, m, b, e = map(int, input().split())
    found = False
    parrent = []
    visited = [0] * (n + 1)
    list_edges = list(map(int, input().split()))
    adj = [[] for i in range(n + 1)]
    k = 0
    for i in range(m):
        u, v = list_edges[k: k + 2]
        adj[u].append(v)
        k += 2

    bfs(b)



if __name__ == "__main__":
    for i in range(int(input())):
        function()
