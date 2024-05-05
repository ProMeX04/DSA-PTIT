
def mul(A, B, n, m):
    C = [0] * ((n - 1) + (m - 1) + 1)
    for i in range(n):
        for j in range(m):
            C[i + j] += A[i] * B[j]
    return C
def function():
    n, m = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    print(*mul(l1, l2, n, m))
if __name__ == "__main__":
    for i in range(int(input())):
        function()