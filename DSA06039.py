from collections import Counter
def function(*line, **kwarg):
    n, A = line
    myDict = Counter(A)

    for i in A:
        if myDict[i] > 1:
            return i

    return "NO"

if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))

