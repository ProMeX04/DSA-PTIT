
def find_ugly_number(current):
    global A
    if current < 1000000000000000000 and current not in A:
        A[current] = 1
        find_ugly_number(current * 2)
        find_ugly_number(current * 3)
        find_ugly_number(current * 5)


def function():
    n = int(input())
    print(ugly_number[n - 1])


if __name__ == "__main__":
    global A
    A = {}
    find_ugly_number(1)
    ugly_number = sorted(A)
    for i in range(int(input())):
        function()
