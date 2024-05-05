# Test sai
from collections import deque

def function():
    n = int(input())
    ls = list(map(int, input().split()))
    ls += [0]
    stack = deque([(ls[0], 0)])
    result = 0
    for index, i in enumerate(ls[1:], start=1):
        k = index
        while stack and stack[-1][0] >= i:
            val, pos = stack.pop()
            if index - pos >= val:
                result = max(result, val)
            k = pos
        stack.append((i, k))
    print(result)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
