
def longgest_commom_subsequence(str1, str2):
    l1, l2 = len(str1), len(str2)
    dp = [0] * l2
    for i in str1:
        maxlen = 0
        for j in range(l2):
            if i == str2[j] and maxlen >= dp[j]:
                dp[j] = maxlen + 1
            else:
                maxlen = max(maxlen, dp[j])
    return max(dp)

def function():
    n, m = input(), input()
    print(longgest_commom_subsequence(n, m))


if __name__ == "__main__":
    for i in range(int(input())):
        function()
