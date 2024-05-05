
def function():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(n)]

    result = 0
    dp = [[0] * (m + 1) for i in range(n + 1)]
    dp[1][1] = 0
    for i in range(1, n + 1):
        for j in range(m + 1):
            d





if __name__ == "__main__":
    for i in range(int(input())):
        function()