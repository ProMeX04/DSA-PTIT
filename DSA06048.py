
def function(*line, **kwarg):
    n, A = line
    return A.index(min(A))

if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int (input()), list(map(int, input().split()))))

