from itertools import combinations
def function():
    n, k = map(int, input().split())
    ls = sorted(list(map(int, input().split())))
    for i in combinations(ls, k):
        print(*i)


if __name__ == "__main__":
    for i in range(int(input())):
        function()