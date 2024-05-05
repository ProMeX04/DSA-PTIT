# tạo xâu s có độ dài 2n + 1

# manacher algorithm
def function():
    s = '$#' + "#".join(input()) + '#!'
    n = len(s)
    dp = n * [1]
    center = right = 0
    for i in range(1,  n - 1):
        if i < right:
            # i < right tức là nó vẫn đang nằm trong xâu đối xứng
            dp[i] = min(right - i, dp[2 * center - i])

        while s[i - dp[i]] == s[i + dp[i]]:
            dp[i] += 1

        if i + dp[i] > right:
            # chuyển sang xâu đối xứng mới
            center, right = i, i + dp[i]

    # print length of longest palindromic substring
    print(max(dp) - 1)


if __name__ == "__main__":
    for i in range(int(input())):
        function()
