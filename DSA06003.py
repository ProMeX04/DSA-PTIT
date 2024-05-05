def function(arr):
    n = len(arr)
    ans = 0
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if arr[j] < arr[k]:
                k = j
        if k != i:
            ans += 1
            arr[k], arr[i] = arr[i], arr[k]
    return ans

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        print(function(a))
