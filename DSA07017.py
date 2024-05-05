from collections import deque
def fn():
    n = int(input())
    ls = list(map(int, input().split()))

    stack = deque([[999999999,0]])
    stack_2 = deque([[-1, 0]])
    result = [-1] * n
    for i in range(n):
        if stack_2:
            while ls[i] < stack_2[-1][0]:
                result[stack_2[-1][1]] = ls[i]
                stack_2.pop()

        if ls[i] <= stack[-1][0]:
            stack.append([ls[i], i])
        else:
            while stack[-1][0] < ls[i]:
                stack_2.append([ls[i], stack[-1][1]])
                stack.pop()
            stack.append([ls[i], i])
    print(*result)


if __name__ == "__main__":
    for i in range(int(input())):
        fn()
