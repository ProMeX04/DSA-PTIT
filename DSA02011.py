from collections import defaultdict


def function():
    n, S = map(int, input().split())
    ls = sorted(list(map(int, input().split())), reverse = True)
    A = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        A[i] = A[i + 1] + ls[i]

    result = float('inf')
    def Try(s, k, j):
        nonlocal result
        if s == S:
            result = k
        elif k < result - 1 and s < S and s + A[j] >= S:
            for i in range(j, n):
                Try(s + ls[i], k + 1, i + 1)

    Try(0, 0, 0)
    print(result if result != float('inf') else -1 )

if __name__ == "__main__":
    for i in range(int(input())):
        function()