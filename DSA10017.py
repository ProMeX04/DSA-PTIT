from collections import defaultdict

def function():
    V, E = map(int, input().split())
    edge_list = []

    while len(edge_list) < E:
        edge_list.append(list(map(int, input().split())))

    d = [1e9] * (V + 1)
    d[1] = 0
    for k in range(V):
        for u, v, w in edge_list:
            if d[u] + w < d[v]:
                d[v] = d[u] + w

    for u, v, w in edge_list:
        if d[u] + w < d[v]:
            return 1
    return 0
    # print(d


if __name__ == "__main__":
    for i in range(int(input())):
        print(function())
