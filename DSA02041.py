from collections import defaultdict

def min_step(n):
    global memory
    if n == 1 or n == 0:
        return 0
    if not memory[n//2]:
        memory[n//2] = min_step(n//2)
    if not memory[n//3]:
        memory[n//3] = min_step(n//3)

    u = memory[n//2] + (n >= 2) + (n%2)
    v = memory[n//3] + (n >= 3) + (n%3)
    
    return min(u, v)
def function():
    global memory
    memory = defaultdict(int)
    n = int(input())
    print(min_step(n))

if __name__ == "__main__":
    for i in range(int(input())):
        function()