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
        self.max_sum = float('-inf')

    def add_node(self, root, parent, child, direction):
        if root is not None:
            if root.value != parent:
                self.add_node(root.left, parent, child, direction)
                self.add_node(root.right, parent, child, direction)

            else:
                if direction == "L":
                    root.add_left(Node(child))
                else:
                    root.add_right(Node(child))

    def make_tree(self, ls):
        self.head = Node(ls[0])
        for i in range(0, 3 * len(ls) // 3, 3):
            self.add_node(self.head, ls[i], ls[i + 1], ls[i + 2])

    def find_max_sum(self, root):
        if root is None:
            return float('-inf')
        if root.is_leaf():
            return root.value    
        l = self.find_max_sum(root.left)
        r = self.find_max_sum(root.right)
        self.max_sum = max(self.max_sum, l + r + root.value)
        return max(l, r) + root.value


def function():
    n = int(input())
    ls = []
    while len(ls) < 3 * n:
        ls += list(map(lambda x: int(x) if x not in ["L", "R"]
                       else x, input().split()))

    tree = Tree()
    tree.make_tree(ls)
    tree.find_max_sum(tree.head)
    print(tree.max_sum)


if __name__ == "__main__":
    for i in range(int(input())):
        function()