
def function():
    k = int(input())
    ls = list(input())
    n = len(ls)
    for i in range(n):
        if k == 0:
            break
        MAX = i
        for j in range(i + 1, n):
            if ls[MAX] <= ls[j]:
                MAX = j
        if MAX != i and ls[MAX] != ls[i]:
            k -= 1
            ls[i], ls[MAX] = ls[MAX], ls[i]

    print("".join(ls))


if __name__ == "__main__":
    for i in range(int(input())):
        function()
