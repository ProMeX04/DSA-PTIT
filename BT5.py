from collections import deque
def function():
    n = int(input())
    s = input().split()

    operator = ['+', '-', '*', '/']
    stack = deque()
    if s[0] in operator:
        s = s[::-1] 
        for i in s:
            if i in operator:
                op1 = stack.pop()
                op2 = stack.pop()
                if i == '/': 
                    i = '//'
                stack.append(str(eval(op1 + i  + op2)))
            else:
                stack.append(i)
    else: 
        for i in s:
            if i in operator:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '/': 
                    i = '//'
                stack.append(str(eval(op1 + i  + op2)))
            else:
                stack.append(i)

    print(stack[0])

if __name__ == "__main__":
    for i in range(int(input())):
        function()