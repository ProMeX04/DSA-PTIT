from queue import Queue

def function(*line, **kwarg):
    n = line[0]
    stack = Queue()
    stack.put(1)
    if n == 1: 
        return 1
    while not stack.empty():

        k = stack.get()
        u = k * 10
        if u % n == 0:
            return u
        else:
            stack.put(u)
        u += 1
        if u % n == 0:
            return u
        else:
            stack.put(u)

        
if __name__ == "__main__":
    for i in range(int(input())):
        print(function(int(input())))
