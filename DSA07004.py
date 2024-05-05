
def function(*line, **kwarg):
    string = line[0]

    stack = []
    for i in string:
        if len(stack) > 0 and i == ")" and stack[-1] == "(":
            if i == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    count_o = 0
    count_c = 0

    for i in stack:
        if i == ")":
            count_c += 1

        else:
            count_o += 1

    return count_c // 2 + count_o // 2 + (count_c%2) * 2
    # print(stack)


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input()))
