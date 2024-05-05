from bisect import bisect_left
def function (*arg, **kwarg): 
    A = []
    for index, i in enumerate(arg[1]):
        k = bisect_left(A, i)
        A.insert(k, i)
        print (f"Buoc {index}:",*A)
    return ""


if __name__ == "__main__":
    print (function(int(input()),list(map(int, input().split()))))