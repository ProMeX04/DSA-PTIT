
def find(j, vC, wC):
    global fopt, n, maxVolume,vpw, xopt, xoptC 
    if j == n:
        fopt = vC
        xopt = xoptC
    else:
        if wC + vpw[0][1] <= maxVolume:
            wN = wC + vpw[j][1]
            vN = vC + vpw[j][0]
            if vN + (maxVolume - wN) * vpw[j + 1][2] > fopt:
                xoptC[j] = 1
                find(j + 1, vN, wN)

        if vC + (maxVolume - wC) * vpw[j + 1][2] > fopt:
            xoptC[j] = 0
            find(j + 1, vC, wC)



def function():
    global fopt, n, maxVolume,vpw, xopt, xoptC
    fopt = -999999999
    n, maxVolume = map(int, input().split())
    xopt = [0] * n
    xoptC = [0] * n
    c = list(map(int, input().split())) + [0]
    w = list(map(int, input().split())) + [9999999]

    vpw = sorted([(a[0],a[1], a[0]/a[1], index) for index, a in enumerate(zip(c, w))], reverse=True,key = lambda x: x[2])

    find(0, 0, 0)
    print (fopt)
    k = sorted(zip(xopt, vpw), key = lambda x: x[1][3])
    for i in k:
        print(i[0] , end= ' ')


if __name__ == "__main__":
    function()
