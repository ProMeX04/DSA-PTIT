def countTriplets(arr, K):
    arr.sort()
    n = len(arr)
    result = 0

    for i in range(n - 2):
        j, k = i + 1, n - 1
        while j < k:
            if arr[i] + arr[j] + arr[k] < K:
                result += (k - j)
                j += 1 
            else:
                k -= 1  
    return result

def main():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        print(countTriplets(A, K))

if __name__ == "__main__":
    main()