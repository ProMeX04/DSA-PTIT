from bisect import bisect_right
def function(*line, **kwarg):
    n, m = line[0]
    A = sorted(line[1])

    for x in range(n - 2):
        i = x + 1
        j = bisect_right(A, m - A[x] - A[i]) - 1
        k = m - A[x]
        while j > i:
            if A[i] + A[j] < k:
                i += 1;
            elif A[i] + A[j] > k:
                j -= 1
            else:
                return "YES" 
    return "NO"


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(map(int, input().split()))))

