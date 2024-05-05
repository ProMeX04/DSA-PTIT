
def function():
    n = int(input())
    j = 1
    while True:
        l = bin(j)[2:].replace("1", "9")
        if int(l) % n == 0:
            print (l) 
            break

        j += 1
if __name__ == "__main__":
    for i in range(int(input())):
        function()