
def function():
    s = input()
    t = len(s)
    dp = [0] * (t + 1)
    for i in range(t):
        dp[i] = dp[i - 1] * 10 + (i + 1) * int(s[i])
    print(sum(dp))


if __name__ == "__main__":
    for i in range(int(input())):
        function()
