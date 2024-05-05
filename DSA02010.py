
def Try(sum, j, result):
    global n, k, nums, ok
    if sum == 0:
        print("[{}]".format(" ".join(result)), end = "")
        ok = True

    elif sum > 0:
        for i in range(j, n):
            Try(sum - nums[i], i, result + str(nums[i]))


def function():
    global n, k, nums, ok 
    ok = False
    n, k = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    Try(k, 0, "")
    if not ok:
        print(-1, end = "")
    print ()


if __name__ == "__main__":
    for i in range(int(input())):
        function()
