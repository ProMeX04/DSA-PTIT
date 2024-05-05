from itertools import product
def function():
    n = int(input())
    count  = 0
    j = 1
    while count < n:
        for i in product(['6','8'], repeat = j):
            k = "".join(i)
            k = k + k[::-1]
            print (k, end = ' ')
            count += 1
            if count >= n:
                break
        j += 1
    print()
if __name__ == "__main__":
    for i in range(int(input())):
        function()