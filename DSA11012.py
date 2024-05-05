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
                
    @staticmethod
    def is_similar(root1, root2):
        if (root1 is None) ^ (root2 is None) or root1.value != root2.value:
            return 0

        else:
            branch_left_similar = branch_right_similar = 1
            if root1.left is not None:
                branch_left_similar = Tree.is_similar(root1.left, root2.left)

            if root1.right is not None:
                branch_right_similar = Tree.is_similar(root1.right, root2.right)

            return branch_left_similar and branch_right_similar


def function():
    n = int(input())
    ls1 = []
    while len(ls1) < 3 * n:
        ls1 += list(map(lambda x: int(x) if x.isdigit()
                        else x, input().split()))
    m = int(input())
    ls2 = []
    while len(ls2) < 3 * n:
        ls2 += list(map(lambda x: int(x) if x.isdigit()
                        else x, input().split()))

    tree1 = Tree()
    tree2 = Tree()

    tree1.make_tree(ls1)
    tree2.make_tree(ls2)

    print(tree1.is_similar(tree1.head, tree2.head))


if __name__ == "__main__":
    for i in range(int(input())):
        function()
