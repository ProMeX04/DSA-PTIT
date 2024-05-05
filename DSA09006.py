from collections import deque


def function():

    v, e, a, b = map(int, input().split())

    adj = [[] for i in range(v + 1)]
    ls = list(map(int, input().split()))

    for i in range(0, 2 * e, 2):
        adj[ls[i]].append(ls[i + 1])
        adj[ls[i + 1]].append(ls[i])

    visited = [0] * (v + 1)
    visited[a] = True

    stack = deque()
    stack.append(a)
    found = False
    while stack and not found:
        top = stack[-1]
        stack.pop()
        for i in adj[top]:
            if not visited[i]:
                visited[i] = True
                stack.append(top)
                stack.append(i)
                if i == b:
                    found = True
                break
    if found:
        print(*stack)
    else:
        print(-1)

if __name__ == "__main__":
    for i in range(int(input())):
        function()