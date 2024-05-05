
def add(k, n, m):
    carry = 0
    A = []
    i = 11
    while n or m:
        s = n % 10 + m % 10 + carry;
        A.append(s % k);
        carry = s // k;
        i -= 1
        n //= 10
        m //= 10
    if carry:
        A.append(carry)
    print("".join(map(str,A[::-1])))

def function():
    k, n, m = map(int, input().split())
    add (k, n, m)

if __name__ == "__main__":
    for i in range(int(input())):
        function()