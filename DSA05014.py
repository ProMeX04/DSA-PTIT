from math import comb, factorial

def function():
    n = int(input())
    print(factorial(2 * n) // factorial(n) // factorial(n + 1))

if __name__ == "__main__":
    for i in range(int(input())):
        function()
