from collections import defaultdict, deque


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
                self.nodes[ls[i]].add_l(self.nodes[ls[i + 1]])
            else:
                self.nodes[ls[i]].add_r(self.nodes[ls[i + 1]])
            head[ls[i + 1]] = False

        for i in head:
            if head[i]:
                self.head = self.nodes[i]
                break

    def spiral_order(self):
        st1 = deque([self.head])
        st2 = deque()
        while st1 or st2:
            while st1:
                top = st1.pop()
                print(top.value, end = " ")
                if top.right is not None:
                    st2.append(top.right)
                if top.left is not None:
                    st2.append(top.left)
                    
            while st2:
                top = st2.pop()
                print(top.value, end = " ")
                if top.left is not None:
                    st1.append(top.left)
                if top.right is not None:
                    st1.append(top.right)
        print()


def function():
    n = int(input())
    ls = []
    while len(ls) < 3 * n:
        ls += list(map(lambda x: int(x) if x.isdigit() else x, input().split()))

    tree = Tree()
    tree.make_tree(ls)
    tree.spiral_order()


if __name__ == "__main__":
    for i in range(int(input())):
        function()