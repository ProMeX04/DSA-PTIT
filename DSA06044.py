
def function (*line, **kwarg): 
    n, A = line
    A[::2],A[1::2] = sorted(A[::2]),sorted(A[1::2], reverse = True)
    return A
    # A[::2] = A[:(n + 1)//2]
    # return A


if __name__ == "__main__":
    print (*function(int(input()), list(map(int, input().split()))))
    