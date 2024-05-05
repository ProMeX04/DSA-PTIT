
def function():
    n = int(input())
    ls1 = list(map(int, input().split()))
    ls2 = list(map(int, input().split()))

    result = sum(map(lambda x, y: x * y, sorted(ls1), sorted(ls2, reverse = True)))
    print(result)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
