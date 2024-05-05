from collections import deque
if __name__ == "__main__":
    myQueue = deque()
    for i in range(int(input())):
        inp = input().split()
        if inp[0] == "PUSHBACK":
            myQueue.append(inp[1])
        elif inp[0] == "PUSHFRONT":
            myQueue.appendleft(inp[1])
        elif inp[0] == "POPBACK":
            try:
                myQueue.pop()
            except:
                continue
        elif inp[0] == "POPFRONT":
            try:
                myQueue.popleft()
            except:
                continue
        elif inp[0] == "PRINTBACK":
            try:
                print(myQueue[-1])
            except:
                print("NONE")
        elif inp[0] == "PRINTFRONT":
            try:
                print(myQueue[0])
            except:
                print("NONE")




