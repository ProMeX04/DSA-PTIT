
def function(*line, **kwarg):
    string = line[0]
    stack = [(")", 0 )]
    result = 0
    for index, i in enumerate(string, start = 1):
        if i == "(":
            stack.append((i,index))
        else:
            if len(stack):
                if stack[-1][0] == ")":
                    stack.append((i, index))

                else:
                    stack.pop()
                    x = stack[-1][1]
                    result = max(result, index - x)

    return result


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input()))
