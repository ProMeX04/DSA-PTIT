from math import perm
def function():
    n, k = map(int, input().split())
    print(perm(n, k) % 1000000007)

if __name__ == "__main__":
    for i in range(int(input())):
        function()