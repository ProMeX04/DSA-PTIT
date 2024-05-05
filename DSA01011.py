def next_permutations():
    global n, ls
    i = len(ls) - 1
    while i >= 1 and ls[i] <= ls[i - 1]:
        i -= 1

    if i == 0:
        return "BIGGEST"

    else:
        for j in range(len(ls) - 1, i - 1, -1):
            if ls[j] > ls[i - 1]:
                ls[j], ls[i - 1] = ls[i - 1], ls[j]
                break
        ls[i:] = reversed(ls[i:])
        return "".join(map(str,ls))


def function():
    global n, ls
    n, ls = input().split()
    n = int(n)
    ls = list(map(int, ls))
    print(n, next_permutations())


if __name__ == "__main__":
    for i in range(int(input())):
        function()
