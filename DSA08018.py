from collections import deque


def function(*line, **kwarg):
    n = line[0]
    print(2**(n + 1) - 2)
    myQueue = deque(["6", "8"])

    while len(myQueue):
        k = myQueue.popleft()
        print(k, end=" ")
        if len(k) < n:
            myQueue.append(k + "6")
            myQueue.append(k + "8")
    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input())))
