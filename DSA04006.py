from math import log, ceil


def function():
    n, l, r = map(int, input().split())

    def length(val):
        if val == 0 or val == 1:
            return 1

        return 2 * length(val // 2) + 1

    def count(pos, val):
        if pos == 0:
            return 0

        half = length(val) // 2

        if pos <= half:
            return count(pos, val // 2)

        elif pos > half:
            return (val + 1) // 2 + count(pos - half - 1, val // 2)

    print(count(r, n) - count(l - 1, n))


if __name__ == "__main__":
    for i in range(int(input())):
        function()