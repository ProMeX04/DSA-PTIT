from collections import deque
def function():
    n, q = map(int,input().split())
    ls = [0]
    while len(ls) < n + 1:
        ls += list(map(int, input().split())) + [-1]
    stack = deque([0])
    dp = [0] * (n + 5)

    for i in range(n, 0, - 1):
        while stack and ls[i] >= stack[-1]:
            stack.pop()
        if not stack:
            dp[i] = 0
        else:
            dp[i] = len(stack)
        stack.append(ls[i])
    for i in range(q):
        print(dp[int(input())])
if __name__ == "__main__":
    function()