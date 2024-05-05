from collections import defaultdict, deque


def function():
    v, e = map(int, input().split())
    ls = list(map(int, input().split()))
    while len(ls) < 2 * e:
        ls += list(map(int, input().split()))

    adj = defaultdict(list)

    for i in range(e):
        adj[ls[2*i]].append(ls[2*i + 1])


    visited = defaultdict(bool)

    def dfs(b_vertex):
        onstack = defaultdict(bool)
        stack = deque()
        stack.append(b_vertex)
        visited[b_vertex] = True
        while stack:
            u = stack.pop()
            onstack[u] = False
            for x in adj[u]:
                if not visited[x]:
                    visited[x] = True
                    onstack[x] = onstack[u] = True
                    stack.append(u) 
                    stack.append(x) 
                    break
                elif onstack[x]:
                    return True

        return False

    for i in range(1, v + 1):
        if not visited[i]:
            if dfs(i):
                return "YES"

    return "NO"
if __name__ == "__main__":
    for i in range(int(input())):
        print(function())
