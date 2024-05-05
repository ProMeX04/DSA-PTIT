
def function(*arg, **kwarg):
    n, m = arg[0]
    print(*set([4,3,5, 2, 7, 1, 9]))
    A, B = set(arg[1]), set(arg[2])
    print(*A|B)
    print(*A & B, end = "")
    return ""

if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(
            map(int, input().split())), list(map(int, input().split()))))