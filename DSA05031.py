dp = [99999] * 10001
B = []
def generate():
    i = 1
    dp[0] = 0
    while i * i <= 10000:
        dp[i * i] = 1
        B.append(i * i)
        i += 1

    for i in range(1, 10001):
        for j in B:
            if j <= i:
                dp[i] = min(dp[i], dp[i - j] + dp[j])
            else: break
    # print(dp)

def function():
    n = int(input())
    print(dp[n])


if __name__ == "__main__":
    generate()
    for i in range(int(input())):
        function()