from collections import deque


def function():
    s = list(input()+"I")

    stack = deque("I")
    find = False
    MIN = 1
    res = ""
    for i in s:
        if i == 'I':
            temp = ""
            while stack:
                temp = str(MIN) + temp
                stack.pop()
                MIN += 1
            res += temp
        stack.append(i)

    print(res)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
