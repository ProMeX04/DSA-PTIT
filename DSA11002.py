from collections import deque


def function(*line, **kwarg):
    n = int(input())
    formulation = input().split()[::-1]
    operator = ['+', '-', '*', '/']
    stack = deque()
    for i in formulation:
        if i not in operator:
            stack.append(i)
        else:
            operand2 = stack.popleft()
            operand1 = stack.popleft()
            if i == '/': 
                i = '//'
            stack.append(str(eval(operand1 + i + operand2)))
    print(stack[0])


if __name__ == "__main__":
    for i in range(int(input())):
        function()
