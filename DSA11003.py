class Node:
    def __init__(self, d=None, l=None, r=None):
        self.d = d
        self.l = l
        self.r = r

    def add_left(self, l=None):
        self.l = l

    def add_right(self, r=None):
        self.r = r


class Tree:
    def __init__(self, head=None):
        self.head = head

    def lrd(self, root):
        if root.l is not None:
            self.lrd(root.l)
        if root.r is not None:
            self.lrd(root.r)
        print(root.d, end=" ")


def function():
    n = int(input())
    ldr = list(map(int, input().split()))
    dlr = list(map(int, input().split()))

    ldr_index = {value: index for index, value in enumerate(ldr)}

    tree = Tree(Node(dlr[0]))
    j = 0
    def find_branch(left, right):
        nonlocal j
        pos = ldr_index[dlr[j]]
        root = Node(dlr[j])
        if pos != left:
            j += 1
            root.add_left(find_branch(left, pos))
        if pos != right - 1:
            j += 1
            root.add_right(find_branch(pos + 1, right))
        return root

    tree.head = find_branch(0, n)
    tree.lrd(tree.head)
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        function()
