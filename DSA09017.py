
def function():
    v = int(input())
    e = v - 1
    ls = []
    for i in range(e):
        ls += map(int ,input().split())
        

    return "YES" if len(set(ls)) == v else "NO"
    


if __name__ == "__main__":
    for i in range(int(input())):
        print(function())
