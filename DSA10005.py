from collections import defaultdict
def function():
    v, e = map(int, input().split())
    ls = list(map(int, input().split()))
    degp = defaultdict(int)
    degm = defaultdict(int)
    for i in range(0, 2*e, 2):
        degp[ls[i]] += 1
        degm[ls[i + 1]] += 1

    cnt = 0
    for i in range(1, v + 1):
        if degp[i] != degm[i]:
            cnt += 1
    print (1 if cnt == 0 else 0)



if __name__ == "__main__":
    for i in range(int(input())):
        function()
