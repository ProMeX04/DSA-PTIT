from itertools import product

def function():
    n = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    for i in product([0, 1], repeat = n):
        result = ""
        Sum = 0;
        for j in range(n):
            if (i[j] == 1):
                result += str(arr[j]) + " "
                Sum += arr[j]
        if Sum %2 == 1:
            print(result)

if __name__ == "__main__":
    for i in range(int(input())):
        function()
