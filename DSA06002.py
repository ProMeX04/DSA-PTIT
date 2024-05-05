
def function(n: int, m: int, arr: list ) -> list:
    return sorted(arr, key=lambda x: abs(x - m))


if __name__ == "__main__":
    for i in range(int(input())):
        n, m = map(int, input().split())
        print(*function(n, m, arr = list(map(int, input().split()))))
