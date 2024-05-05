def function(news: str) -> int:
    if news[0] == '0':
        return 0
    length = len(news)
    dp = [0] * (length + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, length + 1):
        dp[i] = (news[i - 1] != '0') * dp[i - 1] + dp[i - 2] * (int(news[i - 2: i]) <= 26 and int(news[i - 2: i]) >= 10)
    return dp[length]


if __name__ == "__main__":
    for i in range(int(input())):
        print(function(input()))