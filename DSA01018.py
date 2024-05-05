
def function():
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))

    def prev_combine():
        i = k - 1
        while ls[i] == ls[i - 1] + 1:
            i -= 1
        ls[i] -= 1
        for j in range(k-1, i, -1):
            ls[j] = n - k + j + 1
        if i == 0 and ls[i] == 0:
            for i in range(k):
                ls[i] = n - k + i + 1
    prev_combine()
    print(*ls)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
