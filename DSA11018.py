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


class Tree:
    def __init__(self):
        self.head = None
        self.nodes = defaultdict(lambda: None)

    def preorder2bintree(self, ls, n):
        self.head = Node(ls[0])

        def add_node(root, value):
            if value > root.value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    add_node(root.right, value)

            else:
                if root.left is None:
                    root.left = Node(value)
                else:
                    add_node(root.left, value)
        for i in range(1, n):
            add_node(self.head, ls[i])

    def postorder(self):
        def porder(root):        
            if not root:
                return
            porder(root.left)
            porder(root.right)
            print(root.value, end = " ")
        porder(self.head)
        print()

    def pre_order(self):
        def porder(root):
            if not root:
                return
            print(root.value, end = " ")
            porder(root.left)
            porder(root.right)

        porder(self.head)
        print()

def function():
    n = int(input())
    ls = []
    while len(ls) < n:
        ls += list(map(int, input().split()))
    tree = Tree()
    tree.preorder2bintree(ls, n)
    tree.pre_order()


if __name__ == "__main__":
    for i in range(int(input())):
        function()
