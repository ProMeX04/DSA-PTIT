
def function(*line, **kwarg):
    string = line[0]

    opertor = ['+', '-', '*', '/']
    stack = []    
    count = 0
    for i in range(len(string)):
        stack.append(string[i])
        if string[i] in opertor:
            count = 0

        else:
            count += 1
            while count == 2:
                temp = "({1}{2}{0})".format(stack.pop(), stack.pop(), stack.pop())
                stack.append(temp)
                count = 1
                if len(stack) > 1 and stack[-2] not in opertor:
                    count = 2 
    return stack[0]
if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input()))
