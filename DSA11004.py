from collections import defaultdict,deque
class Node:
    def __init__(self, d=None, l=None, r=None):
        self.d = d
        self.l = l
        self.r = r

    def add_left(self, l=None):
        self.l = l

    def add_right(self, r=None):
        self.r = r


def function():
    n = int(input())
    ls = list(map(lambda x: int(x) if x.isdigit() else x,input().split()))

    tree = defaultdict(lambda: None)
    root = defaultdict(lambda: True)

    for i in range(0, 3 * n, 3):
        if tree[ls[i]] is None:
            tree[ls[i]] = Node(ls[i])
            root[ls[i]] = True
        if tree[ls[i + 1]] is None:
            tree[ls[i + 1]] = Node(ls[i + 1])
                
        if ls[i + 2] == "L":
            tree[ls[i]].add_left(tree[ls[i + 1]])

        else:
            tree[ls[i]].add_right(tree[ls[i + 1]])

        root[ls[i + 1]] = False
    def bfs(u):
        queue = deque([u])
        while queue:
            top = queue.popleft()
            print(top, end = ' ')
            if tree[top].l is not None:
                queue.append(tree[top].l.d)
            if tree[top].r is not None:
                queue.append(tree[top].r.d)

    for i in root:
        if i:
            bfs(i)
            break
    print()

if __name__ == "__main__":
    for i in range(int(input())):
        function()