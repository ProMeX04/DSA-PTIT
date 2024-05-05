from itertools import combinations


def next_combine(arr, n, k):
    nums = set(arr)
    i = k
    while arr[i] == n - k + i:
        i -= 1
    if i == 0:
        return k
    else:
        arr[i] += 1
        for j in range(i + 1, k + 1):
            arr[j] = arr[j - 1] + 1
        nums = nums | set(arr)

    return len (nums) - k - 1

def function():
    n, k = map(int, input().split())

    ls = [0] + list(map(int, input().split()))

    print(next_combine(ls, n , k))

if __name__ == "__main__":
    for i in range(int(input())):
        function()
