from collections import deque


def function(*line, **kwarg):
    n = line[0]
    myQueue = deque()
    for i in range(n):
        inp = list(map(int, input().split()))
        if inp[0] == 1:
            print(len(myQueue))
        elif inp[0] == 2:
            if not len(myQueue):
                print("YES")
            else:
                print("NO")
        elif inp[0] == 3:
            myQueue.append(inp[1])

        elif inp[0] == 4:
            try:
                myQueue.popleft()
            except:
                continue

        elif inp[0] == 5:
            try:
                print(myQueue[0])
            except:
                print(-1)

        elif inp[0] == 6:
            try:
                print(myQueue[-1])
            except:
                print(-1)
    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        function(int(input()))
