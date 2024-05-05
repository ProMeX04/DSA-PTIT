ls = []
cnt = 0
def is_special(string):
    global k, cnt
    u = string.find(k * "A")
    if u != -1 and string[u + 1:].find(k * "A") == -1:
       ls.append (string)
       cnt += 1

def Try ( j, string):
    global n, k

    if j != n:
        Try (j + 1, string + "A")
        Try (j + 1, string + "B")
    else:
        if (is_special(string)):
            print (string)

def function (): 
    global n, k
    n, k = map (int, input().split())
    Try (0, "")

    print (cnt)
    for i in ls:
        print (i)



if __name__ == "__main__":
    function()