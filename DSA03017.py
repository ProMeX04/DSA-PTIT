from collections import Counter
def function():
    k = int(input())
    ls = sorted(Counter(input()).values())
    
    total = sum(ls) - k
    numChar = len(ls)
    average = total / numChar
    result = 0 

    for i in ls:
        if i <= average:
            result += i * i
            numChar -= 1
            total -= i
            average = total / numChar
        else:
            result += (total // numChar) ** 2
            total -= total // numChar
            numChar -= 1 

    print(result)




    

if __name__ == "__main__":
    for i in range(int(input())):
        function()