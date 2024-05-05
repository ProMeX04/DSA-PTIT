from collections import deque

def function():
    formulation = input()
    while not len(formulation):
        formulation = input()
    stack = deque()
    operator = ['+', '-', '*', '/']
    for i in formulation:
        if i not in operator:
            stack.append(i)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 + i + operand2)

    print(*stack)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
