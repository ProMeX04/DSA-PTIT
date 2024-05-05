import heapq

def maximize_profit():
    n = int(input())
    jobs = [tuple(map(int, input().split()))[1:] for _ in range(n)]
    jobs.sort(reverse=True)

    q, result, cv = [], 0, 0
    deadline, i = jobs[0][0], 0

    while deadline > 0:
        while i < n and jobs[i][0] == deadline:
            heapq.heappush(q, -jobs[i][1])
            i += 1
        deadline -= 1
        if q:
            cv += 1
            result -= heapq.heappop(q)

    print(cv, result)

def main():
    t = int(input())
    for _ in range(t):
        maximize_profit()

if __name__ == "__main__":
    main()
