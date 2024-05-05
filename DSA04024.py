
def function():
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    ls.sort()

    i, j = 0, 1
    count = 0
    while i < len(ls):
        while j < n and ls[j] - ls[i] < k:
            j += 1

        count += j - i - 1
        i += 1

    print(count)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
