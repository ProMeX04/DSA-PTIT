import heapq


def function():
    n = int(input())
    ls = list(map(int, input().split()))

    heapq.heapify(ls)

    result = 0
    while len(ls) > 1:
        top1 = ls[0]
        heapq.heappop(ls)
        top2 = ls[0]
        heapq.heappop(ls)
        result += top1 + top2
        result %= 1000000007
        heapq.heappush(ls, (top1 + top2) % 1000000007)
    print(result)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
