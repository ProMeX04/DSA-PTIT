t = int(input())
for _ in range(t):
    k = int(input())
    s = input().split()
    print(s)
    st = []
    p = -1
    for i in range(len(s)):
        print(i)
        if s[i].isdigit():
            st.append(int(s[i]))
            p += 1
        elif s[i] == '*':
            st[p - 1] *= st[p]
            p -= 1
        elif s[i] == '/':
            st[p - 1] //= st[p]
            p -= 1
        elif s[i] == '+':
            st[p - 1] += st[p]
            p -= 1
        elif s[i] == '-':
            st[p - 1] -= st[p]
            p -= 1


    print(st[0])
