
def function (): 
    ls = []
    while True:
        try:
            ls += list(map(int, input().split()))
        except:
            break
    n, m = ls[:2]   
    ls = ls[2:]


    minBill = [99999999] * (m + 1)
    minBill[0] = 0
    for i in range(n):
        for j in range(m, -1 , -1):
            if ls[i] + j <= m:
                minBill[ls[i] + j] = min(minBill[ls[i] + j], minBill[j] + 1)
    if minBill[m] != 999999999:
        print(minBill[m])
    else:
        print(-1)



if __name__ == "__main__":
    function()