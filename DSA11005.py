
from collections import deque


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.value = value
        self.right = right

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right


class Tree:
    def __init__(self):
        self.head = None

    def print_tree(self, head):
        if head is not None:
            if head.left is not None:
                self.print_tree(head.left)
            if head.right is not None:
                self.print_tree(head.right)
        print(head.value, end=" ")


def function():
    n = int(input())
    in_order = list(map(int, input().split()))
    lev_order = list(map(int, input().split()))

    index = dict([i, index] for index, i in enumerate(in_order))
    j = 0

    def make_tree():
        nonlocal j
        tree = Tree()
        tree.head = Node(lev_order[0])
        queue = deque([tree.head])

        while queue:
            root = queue.popleft()
            top = root.value
            pos = index[top]
            if j + 1 < n and index[lev_order[j + 1]] < pos:
                j += 1
                root.add_left(Node(lev_order[j]))
                queue.append(root.left)
            if j + 1 < n and index[lev_order[j + 1]] > pos:
                j += 1
                root.add_right(Node(lev_order[j]))
                queue.append(root.right)
        return tree

        
    tree = make_tree()
    tree.print_tree(tree.head)
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        function()
