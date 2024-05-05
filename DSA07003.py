from collections import deque


def function(*line, **kwarg):
    string = line[0]
    stack = [0]
    for i in string:
        if i == "(":
            stack.append(0)

        elif i in ['+', '-', '*', '/']:
            stack[-1] += 1

        elif i == ")":
            if len(stack) > 1 and stack[-1] == 0:
                return "Yes"
            try:
                stack.pop()
            except:
                return "Yes"
    if len(stack) > 1:
        return "Yes"
    return "No"


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input()))
