from collections import Counter
def function():
    n, v = map(int, input().split())
    odds = len(list(filter(lambda x: x % 2 == 1, Counter(map(int, input().split())).values())))
    if odds == 2:
        print(1)
    elif odds == 0:
        print(2)
    else:
        print(0)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
