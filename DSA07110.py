
def function(*line, **kwarg):
    string = line[0]
    stack = []
    p = 0
    openw = {")" : "(", "]" : "[", "}":"{"}
    for i in string:
        if i not in openw:
            stack.append(i)
        elif len(stack) and openw[i] == stack[-1]: 
            stack.pop()
        else:
            return "NO"
    if len(stack):
        return "NO"
    return "YES"

if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input()))
