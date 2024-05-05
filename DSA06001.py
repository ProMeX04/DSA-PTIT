def function(n: int, arr: list) -> list:
    arr.sort()
    arr[1::2], arr[::2] = arr[:n//2], arr[-1:n//2 - 1: -1] 
    return arr


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        print(*function(n, arr))