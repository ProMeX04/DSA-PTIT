
def function():
    n, m = map (str, input().split())
    print(int(n,2) * int(m, 2))

if __name__ == "__main__":
    for i in range(int(input())):
        function()