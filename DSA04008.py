
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

    n = int(input())
    if n == 0:
        print(0)
    C = pow_mod([[1,1],[1,0]], n - 1)
    print(C[0][0])

if __name__ == "__main__":
    for i in range(int(input())):
        function()