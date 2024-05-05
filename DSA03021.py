
def find_nums(n, k):
    X = n // k
    if n == k:
        return 1

    while n // X == k:
        X -= 1

    if n // (X + 1) == k:
        return X + 1
    else:
        return -1


def function():
    n = int(input())
    ls = list(map(int, input().split()))
    M = min(ls)
    for j in range(M, 0, -1):
        result = 0
        ok = True
        for i in ls:
            t = find_nums(i, j)
            if t ==  -1:
                ok = False
                break
            else:
                result += t
        if ok:
            print(result)
            break

    # tìm số nhỏ nhất
    # k càng lớn thì dãy càng nhỏ
    # Duyệt k giảm dần từ số nhỏ nhất về 0
    # tìm số nhỏ nhất x / số đó // x == k
    # k * x <= ls[i] (x = ?)
    #
    # (k + 1)x >= lx[i] + 1
    # x = ls[i] + 1 // (k + 1)

if __name__ == "__main__":
    function()
