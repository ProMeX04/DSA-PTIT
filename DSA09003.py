# from collections import defaultdict

def function(*line, **kwarg):
    vertex, edge = line[0]

    adj = [[] for i in range(vertex + 1)]
    for i in range(edge):
        u, v = map(int, input().split())
        adj[u].append(v)

    for i in range(vertex):
        print (f"{i + 1}:",*adj[i + 1])
if __name__ == "__main__":
    for i in range(int(input())):
        function(map(int, input().split()))
