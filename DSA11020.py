def function():
    n = int(input())
    ls = []
    while len(ls) < n:
        ls += list(map(int, input().split()))

    for i in range(1,n):
        if ls[i] <= ls[i - 1]:
            print(0)
            return
    print(1)

if __name__ == "__main__":
    for i in range(int(input())):
        function()