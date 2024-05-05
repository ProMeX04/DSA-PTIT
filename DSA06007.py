
    def function(*arg, **kwarg):
        n, A = arg[0], arg[1]
        B = sorted(A)
        left = 0
        right = n - 1
        for i in range(n):
            if A[i] != B[i]:
                left = i
                break;
        for i in range(n - 1, 0, - 1):
            if A[i] != B[i]:
                right = i
                break;


        return left + 1, right + 1
    if __name__ == "__main__":
        for i in range(int(input())):
            print(*function(int(input()), list(map(int, input().split()))))

