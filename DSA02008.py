from itertools import permutations
def function():
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(n)]
    per = [i + 1 for i in range(n)]
    ls_result = []
    for i in permutations(per):
        total = 0
        for j in range(n):
            total += matrix[j][i[j] - 1]
        if total == k:
            ls_result.append(i)
    
    print (len(ls_result))
    for i in ls_result:
        print (*i)



if __name__ == "__main__":
    function()