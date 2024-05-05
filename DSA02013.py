from bisect import bisect_right


def sieve():
    ls = []
    MAX = 201
    A = [0] * (MAX + 1)
    i = 2
    while i * i < MAX:
        if not A[i]:
            j = i * i
            while j < MAX:
                A[j] = True
                j += i
        i += 1
    for i in range(2, MAX):
        if not A[i]:
            ls.append(i)
    return ls


def Try(j, summ, result, t):
    global ls, prime, cnt, n, s
    if t == n:
        if summ == s:
            ls.append(result.rstrip())
            cnt += 1
    else:
        while summ + prime[j] <= s:
            Try(j + 1 , summ + prime[j], result + f"{prime[j]} ",t + 1)
            j += 1


def function(prime):
    global ls, cnt, n, s
    cnt = 0
    ls = []
    n, p, s = map(int, input().split())
    k = bisect_right(prime, p)
    Try(k, 0, "", 0)
    print(cnt)
    for i in ls:
        print(i)


if __name__ == "__main__":
    global prime
    prime = sieve()
    for i in range(int(input())):
        function(prime)
