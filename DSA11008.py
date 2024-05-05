from collections import defaultdict,deque
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def add_r(self, right):
        self.right = right

    def add_l(self, left):
        self.left = left

    def is_leaf(self):
        return self.left is None and self.right is None

class Tree:
    def __init__(self):
        self.head = None
        self.tree_dict = defaultdict(lambda : None)

    def check_leaf(self):
        queue = deque([(self.tree_dict[self.head], 1)])
        while queue:
            top = queue.popleft()
            u = top[0]
            exp = top[1]

            if u.is_leaf():
                k = exp
                break

            if u.left is not None: 
                queue.append([u.left, exp + 1])

            if u.right is not None:
                queue.append([u.right, exp + 1])

        for i in queue:
            if k != i[1]:
                return 0
        return 1
def function():
    n = int(input())
    ls = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
    tree = Tree()
    head = defaultdict(lambda : True)
    for i in range(0, 3 * n, 3):
        if tree.tree_dict[ls[i]] is None:
            head[ls[i]] = True
            tree.tree_dict[ls[i]] = Node(ls[i])
        if tree.tree_dict[ls[i + 1]] is None:
            tree.tree_dict[ls[i + 1]] = Node(ls[i + 1])
        if ls[i + 2] == "L":
            tree.tree_dict[ls[i]].add_l(tree.tree_dict[ls[i + 1]])
        else:
            tree.tree_dict[ls[i]].add_r(tree.tree_dict[ls[i + 1]])
        head[ls[i + 1]] = False

    for i in head:
        if head[i]:
            tree.head = i
            break

    print(tree.check_leaf())
if __name__ == "__main__":
    for i in range(int(input())):
        function()
