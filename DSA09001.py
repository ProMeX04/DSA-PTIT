from collections import defaultdict
def function(*line, **kwarg):
    n, m = line[0]

    A = [[] for i in range(n + 1)]

    for i in range(m):
        u, v = map(int, input().split())
        A[u].append(v)
        A[v].append(u)

    for i in range(1, n + 1):
        print(f"{i}:", *A[i])
    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split())),end = "")
