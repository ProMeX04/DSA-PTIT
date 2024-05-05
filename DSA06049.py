def function(*line, **kwarg):
    n, m = line[0]
    A = sorted(line[1])

    result = 0

    r = 0;

    for i in range(n - 1):
        while r < n and A[r] - A[i] < m:
            r += 1
        result += r - i - 1
    return result



if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(map(int, input().split()))))

