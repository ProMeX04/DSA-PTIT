from collections import deque

def function():
    s = list(input())
    stack = deque()
    operator = ['+','-','*','/']
    for i in s:
        if i in operator:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append("({}{}{})".format(op1,i,op2))
        else:
            stack.append(i)
    print(*stack)

if __name__ == "__main__":
    for i in range(int(input())):
        function()