
def function(*line, **kwarg):
    n, A = line

    stack = [(99999999999999999999,-1)]
    B = [-1] * n
    for index,i in enumerate(A):
        while i > stack[-1][0]:
            B[stack.pop()[1]] = i
        stack.append((i, index))

    for i in B:
        print (i, end = ' ')
    return ""

if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input()), list(map(int, input().split()))))

