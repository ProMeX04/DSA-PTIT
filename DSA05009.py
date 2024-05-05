def function(n: int, arr: list) -> str:
    S = sum(arr)
    if S % 2 == 1:
        return "NO"

        
    S = S // 2
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in arr:
        for j in range(S, 0, -1):
            if i <= j and dp[j - i]:
                dp[j] = 1

    
    return "YES" if dp[S] else "NO"


def main():
    for i in range(int(input())):
        n = int(input())
        print(function(n, sorted(list(map(int, input().split())))))


if __name__ == "__main__":
    main()