from collections import Counter


def function():
    n = int(input())
    s1 = input()
    s2 = sorted(s1, reverse=True)
    pair = zip(s1, s2)
    count = Counter(pair)

    u = count[('T', 'T')] + count[('D', 'D')] + count[('X', 'X')]
    v = min(count[('T', 'X')], count[('X', 'T')]) + min(count[('T', 'D')],
                                                        count[('D', 'T')]) + min(count[('X', 'D')], count[('D', 'X')])
    n -= u + 2 * v

    print(v + 2*n // 3)


if __name__ == "__main__":
    function()
