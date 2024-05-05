from collections import defaultdict, deque

def function():
    v, e = map(int, input().split())
    ls = list(map(int, input().split()))

    while len(ls) < 2 * e:
        ls += list(map(int, input().split()))

    adj = defaultdict(list)
    for i in range(0, 2 * e, 2):
        adj[ls[i]].append(ls[i + 1])

    visited = defaultdict(bool)

    def dfs(bVertex):
        stack = deque()
        stack.append(bVertex)
        visited[bVertex] = True
        onstack = defaultdict(int)
        while stack:
            u = stack.pop()
            onstack[u] = False
            for x in adj[u]:
                if not visited[x]:
                    visited[x] = True
                    onstack[x] = True
                    onstack[u] = True
                    stack.append(u)
                    stack.append(x)
                    break
                elif onstack[x]:
                    return True
        return False

    for i in range(1, v + 1):
        if not visited[i]:
            if dfs(i):
                return True

    return False


if __name__ == "__main__":
    for i in range(int(input())):
        print("YES" if function() else "NO")
