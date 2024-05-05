def function():
    n = int(input())
    for i in range(1<<n):
        print(bin(i ^ (i >> 1))[2:].zfill(n), end = " ")
    print ()


if __name__ == "__main__":
    for i in range(int(input())):
        function()