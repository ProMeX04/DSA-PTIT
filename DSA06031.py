from collections import deque


def function(*arg, **kwarg):
    n, k = arg[0]
    A = arg[1]

    myQueue = deque()
    for i in range(n):
        while len(myQueue) != 0 and A[myQueue[-1]] <= A[i]:
            myQueue.pop()
        myQueue.append(i)
        if myQueue[0] + k <= i:
            myQueue.popleft()
        if i >= k - 1:
            print(A[myQueue[0]], end=" ")

    return ""


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(map(int, input().split()), list(map(int, input().split()))))
