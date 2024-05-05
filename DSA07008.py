from collections import deque


def function():
    inp = list(input())
    stack = deque()
    pri_op = {}
    pri_op['+'] = 1
    pri_op['-'] = 1
    pri_op['*'] = 2
    pri_op['/'] = 2
    pri_op['^'] = 3
    
    i = 0

    def object(level, prevObject=None, xopen = False):
        nonlocal i
        stack = deque()
        if prevObject:
            stack.append(prevObject)

        while i < len(inp):
            if inp[i] == '(':
                i += 1
                stack.append(object(1, xopen = True))

            elif inp[i] == ')':
                i += xopen
                break

            elif inp[i] in pri_op and pri_op[inp[i]] > level:
                stack.append(object(pri_op[inp[i]], stack.pop()))

            elif inp[i] in pri_op and pri_op[inp[i]] < level:
                break

            else:
                stack.append(inp[i])
                i += 1

        while len(stack) > 1:
            op1 = stack.popleft()
            op = stack.popleft()
            op2 = stack.popleft()
            stack.appendleft("{}{}{}".format(op1, op2, op))
        return stack[0]
    res = object(0)
    print(res)


if __name__ == "__main__":
    for i in range(int(input())):
        function()