
def function():
    n = int(input())
    c4 = 0
    while n % 7 != 0 and n >= 0:
        c4 += 1
        n -= 4
    if n < 0:
        print(-1)

    else:
        print(c4*"4"+(n //7) * "7")
if __name__ == "__main__":
    for i in range(int(input())):
        function()