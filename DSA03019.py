
def function():
    a, b = map(int, input().split())
    while b % a:
        x = ( b+ a - 1) // a
        print(f"1/{x}", end = " + ")
        a = (a * x - b)
        b = x * b
    print(f"1/{( b+ a - 1) // a}")
if __name__ == "__main__":
    for i in range(int(input())):
        function()