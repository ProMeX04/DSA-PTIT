from collections import deque
def function():
    v ,e = map(int, input().split())
    ls = list(map(int, input().split()))
    adj = [[] for i in range(10001)]
    iadj = [[] for i in range(10001)]

    for i in range(0, 2 * e, 2):
        adj[ls[i]].append(ls[i + 1])
        iadj[ls[i + 1]].append(ls[i])

    def kosaraju(u, xadj):
        visited = [0] * (10001)
        stack = deque()
        stack.append(u)
        visited[u] = True
        while stack:
            top = stack.pop()
            for x in xadj[top]:
                if not visited[x]:
                    visited[x] = True
                    stack.append(top)
                    stack.append(x)
                    break
        if visited.count(1) != v:
            return False
        return True

    if kosaraju(1, adj) and kosaraju(1,iadj):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    for i in range(int(input())):
        function()