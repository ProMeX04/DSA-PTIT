
def merge(left, right):
    global n, ls, res
    mid = (left + right) // 2
    A = ls[left:mid]
    B = ls[mid:right]
    i = j = 0
    k = left
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            ls[k] = A[i]
            i += 1
        else:
            ls[k] = B[j]
            j += 1
            res += len(A) - i
        k += 1

    while i < len(A):
        ls[k] = A[i]
        i += 1
        k += 1

    while j < len(B):
        ls[k] = B[j]
        j += 1
        k += 1
    


def merge_Sort(left, right):
    global n, ls
    if left < right - 1:
        mid = (left + right) // 2
        merge_Sort(left, mid) 
        merge_Sort(mid, right)
        merge(left, right)

def function():
    global n, ls, res
    res = 0
    n = int(input())
    ls = list(map(int, input().split()))
    merge_Sort(0, n)
    print(res)
    # merge(0, n - 1)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
