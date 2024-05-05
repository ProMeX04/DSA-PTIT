from collections import deque

if __name__ == "__main__":
    myQueue = deque()
    n = int(input())
    for i in range(n):
        inp = input().split()
        if inp[0] == "PUSH":
            myQueue.append(inp[1])
        elif inp[0] == "POP":
            try:
                myQueue.popleft()
            except:
                continue
        elif inp[0] == "PRINTFRONT":
            try:
                print(myQueue[0])
            except:
                print("NONE")