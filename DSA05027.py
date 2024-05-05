def function(n: int, v: int, product: list) -> int:
    dp = [0] * (v + 1)
    dp[0] = 0
    for pd in product:
        for j in range(v, 0, -1):
            if j - pd[0] >= 0:
                dp[j] = max(dp[j], dp[j - pd[0]] + pd[1])
    return dp[v]


if __name__ == "__main__":  
    for i in range(int(input())):
        n, v = map(int, input().split())
        product = [(a, b) for a, b in zip(
            list(map(int, input().split())), list(map(int, input().split())))]
        # product.sort()
        print (product)    
        print(function(n, v, sorted(product)))
