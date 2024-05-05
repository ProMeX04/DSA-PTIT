
from collections import defaultdict, deque


def function():
    n = int(input())
    ls = []
    while len(ls) < n - 1:
        ls += list(map(int, input().split()))
    tree = defaultdict(list)

    value = defaultdict(lambda: list([1,1]))

    for i in range(2, n + 1):
        tree[ls[i - 2]].append(i)

    def transfer(u):
        stack = deque([u])
        parent = defaultdict(int)
        parent[1] = 1
        while stack:
            top = stack[-1]
            change = False
            for i in tree[top]:
                if not value[i]:
                    stack.append(i)
                    parent[i] = top
                    change = True
                    break
            if not change:
                stack.pop()
                if top != 1:
                    value[parent[top]][0] += value[top][0] + value[top][1]
                    value[parent[top]][1] += value[top][1]
    transfer(1)
    for i in value.values():
        print(i[0], end=" ")


if __name__ == "__main__":
    function()
