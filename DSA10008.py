


from collections import defaultdict
from heapq import *

def function():
    v, e, begin = map(int, input().split())
    adj = defaultdict(list)
    for i in range(e):
        b, x, w = map(int, input().split())
        a
        

    ls = [(0, begin)]
    heapify(ls)
    cost = [float('inf')] * (v + 1)
    cost[begin] = 0
    visited = defaultdict(bool)

    while ls:
        w, top = heappop(ls)
        if visited[top]:
            continue
        visited[top] = True
        for edge in adj[top]:
            if cost[top] + edge[1] < cost[edge[0]]:
                cost[edge[0]] = cost[top] + edge[1]
                heappush(ls, (cost[edge[0]], edge[0]))
    print(*cost[1:v + 1])


if __name__ == "__main__":
    for _ in range(int(input())):
        function()
