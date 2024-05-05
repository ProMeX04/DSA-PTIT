
def mul(A, B):
    n, m, p = len(A) , len(A[0]), len(B[0])

    C = [[0] * n for i in range(p)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= 1000000007
    return C

def pow_mod (A, n):
    if n == 1:
        return A
    temp = pow_mod(A, n//2)
    if n&1:
        return mul(mul(temp, temp),A)
    return mul(temp, temp)

def function():   
    n, m = map (int, input().split())
    A = [list(map(int, input().split()))for i in range(n)]
    C = pow_mod(A, m)
    for i in C:
        print(*i)

if __name__ == "__main__":
    for i in range(int(input())):
        function()