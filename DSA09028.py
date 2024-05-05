from collections import defaultdict, deque


def function():
    v, e, M = map(int, input().split())
    adj = defaultdict(list)

    for i in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    
    cantUse = [[False] * (M + 1) for i in range(v + 1)]
    color = defaultdict(int)
   

    for i in adj:
        if not color[i]:
            queue = deque([i])
            while queue:
                top = queue.popleft()
                for j in range(1, M + 1):
                    if cantUse[top][j] == False:
                        color[top] = j
                        break

                if not color[top]:
                    return False

                for x in adj[top]:
                    if not color[x]:
                        cantUse[x][color[top]] = True
                        queue.append(x)
    return True


if __name__ == "__main__":
    for i in range(int(input())):
        print("YES" if function() else "NO")
