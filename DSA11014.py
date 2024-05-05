from collections import defaultdict
class Node:
    def __init__(self, val = None, left = None, right = None): 
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

class Tree:
    def __init__(self, head = None):
        self.head = head
        self.listNode = defaultdict(lambda : None)

    def make_tree(self, ls, n):
        for i in range(n):
            r, c, w = int(ls[3 * i]), int(ls[3 * i + 1]), ls[3 * i + 2]
            if self.head is None:
                self.head = Node(r)
                self.listNode[r] = self.head

            self.listNode[c] = Node(c)

            if w == 'L':
                self.listNode[r].left = self.listNode[c]
            else:
                self.listNode[r].right = self.listNode[c]

    def print_pre_order(self):

        def loop(root):
            print(root.val , end = " ")
            if root.left:
                loop(root.left)

            if root.right:
                loop(root.right)
        loop(self.head)
        print()

    def sum_right_leaf(self):
        total = 0
        def loop(root):
            nonlocal total
            if root.left:
                loop(root.left)

            if root.right:
                if root.right.is_leaf():
                    total += root.right.val

                loop(root.right)

        loop(self.head)
        return total

def function():
    n = int(input())
    ls = input().split()

    tree = Tree()
    tree.make_tree(ls, n)
    print(tree.sum_right_leaf())



if __name__ == "__main__":
    for i in range(int(input())):
        function()