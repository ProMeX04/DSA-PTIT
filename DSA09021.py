
def function():
    n = int(input())
    adj = [[]for i in range(n)]
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(n):
            if arr[j]:
                adj[i].append(j + 1)

        print(*adj[i])


if __name__ == "__main__":
    function()
