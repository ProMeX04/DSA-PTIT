
def Try(n, ls, min=0, result=""):
    print(result, end = " ")
    for i in range(min, n):
        Try(n, ls, i + 1, result + ls[i])

def function():
    n = int(input())
    ls = sorted(list(input()))
    Try(n, ls)
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        function()
