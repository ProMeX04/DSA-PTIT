
def function(*line, **kwarg):
    n, A = line
    A = list(map(lambda x: x*x, A))
    A.sort()
    for i in range (n - 1, 0, -1):
        l, r = 0, i - 1
        while r > l:
            if A[l] + A[r] == A[i]:
                return "YES"
            elif A[l] + A[r] < A[i]:
                l += 1 
            else:
                r -= 1
    return "NO"


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))

