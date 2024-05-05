from collections import deque
def function():
    s = list(input())

    stack = deque()
    operator = ['+','-','*','/']
    for i in s:
        if i in operator:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append("{}{}{}".format(i,op1,op2))
        else:
            stack.append(i)
    print(stack[0])
if __name__ == "__main__":
    for i in range(int(input())):
        function()