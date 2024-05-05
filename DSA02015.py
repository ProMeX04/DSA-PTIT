from collections import Counter


def function():
    inp = list(input())
    freq = Counter(inp)
    print(freq)

    r_open = r_close = 0
    if freq[')'] == 0 or freq['('] == 0:
        print(-1)
        return

    if freq[')'] > freq['(']:
        r_close = freq[')'] - freq['(']
    elif freq[')'] < freq['(']:
        r_open = freq['('] - freq[')']
    else:
        r_close = r_open = 1
    print(r_close, r_open)
    result = set()
    k = ""
    x_open = 0
    for i in range(n):
        if inp[i] == '(':
            x_open += 1
        if inp[i] == ')':
            if x_open > 0



if __name__ == "__main__":
    for i in range(int(input())):
        function()
