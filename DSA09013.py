def tarjan(cur):
    global count, adj, low, num, par, res

    num[cur] = low[cur] = count
    count += 1

    for nex in adj[cur]:
        if not num[nex]:
            par[nex] = cur
            tarjan(nex)
            low[cur] = min(low[cur], low[nex])
        elif par[cur] != nex:
            low[cur] = min(low[cur], num[nex])

    # print(cur ,low, num, par)

    # sau khi duyệt qua các cạnh kề cạnh hiện tại
    if num[cur] == low[cur]:
    #     res += 1
    #     temp = cur
    #     print (low, num)
    #     low[cur] = 99999999999
    #     while temp != par[temp]:
    #         temp = par[temp]
    #         low[temp] = 99999999999

def function():
    vertex, edge = map(int, input().split())

    global count, adj, low, num, par, res
    res = 0
    count = 1
    low = (vertex + 1) * [0]
    num = (vertex + 1) * [0]
    par = (vertex + 1) * [0]
    par[1] = 1
    adj = [[] for i in range(vertex + 1)]

    for i in range(edge):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    tarjan(1)
    print(low, num , par)

if __name__ == "__main__":
    for i in range(int(input())):
        function()
