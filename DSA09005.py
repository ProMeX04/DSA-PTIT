from queue import Queue
from itertools import * 
def bfs(s, visited, adj):
    myQueue = Queue()
    myQueue.put(s)
    while not myQueue.empty():
        current = myQueue.get()
        print(current, end=" ")
        visited[current] = True
        for i in adj[current]:
            if not visited[i]:
                myQueue.put(i)
                visited[i] = True


def function(*line, **kwarg):
    v, e, s = line[0]
    A = list(map(int, input().split()))
    adj=[[] for i in range(v + 1)]
    visited=[False] * (v + 1)

    k=0

    for i in range(e):
        adj[A[k]].append(A[k + 1])
        adj[A[k + 1]].append(A[k])
        k += 2
    bfs(s, visited, adj)
    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split())))
