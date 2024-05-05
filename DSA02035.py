from itertools import permutations


def function (): 
    n, k = map(int , input().split())
    ls = [list(map(int,list(input()))) for i in range(n)]

    pos = [i for i in range(0, k)]
    ans = 999999999999999
    for i in permutations(pos):
        Min, Max = 9999999999999999 , 0
        for j in range(n):
            nums = 0
            for _ in range(k):
                nums = nums * 10 + ls[j][i[_]]
            Min = min(Min, nums)
            Max = max(Max, nums)
        ans = min(ans, Max - Min)
    print (ans)
if __name__ == "__main__":
    function()