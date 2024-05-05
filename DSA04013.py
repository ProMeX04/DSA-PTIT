
def function():
    n = int(input())
    ls = list(map(int, input().split()))
    ls.sort()
    j = n//2
    i = 0
    count = n
    while j < n:
        while j < n and ls[i] * 2 > ls[j]:
            j += 1
        if j < n:
            count -= 1
            j += 1
        i += 1
    print(count)
if __name__ == "__main__":
    for i in range(int(input())):
        function()