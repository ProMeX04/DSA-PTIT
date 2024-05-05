from collections import deque


def function(*line, **kwarg):
    n = line[0]
    print(2**(n + 1) - 2)
    myQueue = deque(["6", "8"])
    stack = []
    while len(myQueue):
        k = myQueue.popleft()
        stack.append(k)
        if len(k) < n:
            myQueue.append(k + "6")
            myQueue.append(k + "8")
    print(*stack[::-1], end="")
    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input())))
