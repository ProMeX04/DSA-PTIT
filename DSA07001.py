from collections import deque
if __name__ == "__main__":
    myQueue = deque()
    for i in range(int(input())):
        method = input().split()        
        if method[0] == "PUSH":
            myQueue.append(int(method[1]))
        elif method[0] == "PRINT":
            if len(myQueue) > 0:
                print (myQueue[-1])
            else:
                print ("NONE")
        elif method[0] == "POP":
            try:
                myQueue.pop()
            except:
                ...