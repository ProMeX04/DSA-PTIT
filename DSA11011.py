from collections import defaultdict, deque


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def add_right(self, right):
        self.right = right

    def add_left(self, left):
        self.left = left

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_perfect(self):
        return self.left is not None and self.right is not None


class Tree:
    def __init__(self):
        self.head = None
        self.nodes = defaultdict(lambda: None)

    def make_tree(self, ls):
        head = defaultdict(lambda: True)
        for i in range(0, 3 * len(ls) // 3, 3):
            if self.nodes[ls[i]] is None:
                head[ls[i]] = True
                self.nodes[ls[i]] = Node(ls[i])
            if self.nodes[ls[i + 1]] is None:
                self.nodes[ls[i + 1]] = Node(ls[i + 1])
            if ls[i + 2] == "L":
                self.nodes[ls[i]].add_left(self.nodes[ls[i + 1]])
            else:
                self.nodes[ls[i]].add_right(self.nodes[ls[i + 1]])
            head[ls[i + 1]] = False

        for i in head:
            if head[i]:
                self.head = self.nodes[i]
                break

    def is_full(self):
        queue = deque([self.head])
        while queue:
            top = queue.pop()
            if top.is_perfect():                
                queue.append(top.left)
                queue.append(top.right)
            elif not top.is_leaf():
                return 0
        return 1


def function():
    n = int(input())
    ls = []
    while len(ls) < 3 * n:
        ls += list(map(lambda x: int(x) if x.isdigit() else x, input().split()))

    tree = Tree()
    tree.make_tree(ls)
    print(tree.is_full())


if __name__ == "__main__":
    for i in range(int(input())):
        function()