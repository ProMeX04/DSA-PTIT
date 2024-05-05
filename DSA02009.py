def function():
    n, k = map(int, input().split())
    ls = sorted(list(map(int, input().split())))
    total = sum(ls)

    def Try(total_sub, subs):
        if subs == k:
            return 1

        elif total_sub == sum_of_subs:
            if Try(0, subs + 1):
                return 1

        elif total_sub < sum_of_subs:
            for i in range(n):
                if Try(total_sub + ls[i], subs):
                    return 1
        return 0
    if total % k == 0:
        sum_of_subs = total // k
        print(Try(0, 0))
    else:
        print(0)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
