class Node:
    def __init__(self, value=None, exp=None):
        self.value = value
        self.exp = exp
        self.next = None


class Formulation:
    def __init__(self):
        self.head = None

    def insert(self, value, exp):
        if self.head is None:
            self.head = Node(value, exp)
            return

        if exp == self.head.exp:
            self.head.value += value
            return

        if exp > self.head.exp:
            temp = self.head
            self.head = Node(value, exp)
            self.head.next = temp
            return

        temp = self.head
        while temp.next is not None and temp.next.exp > exp:
            temp = temp.next


        if temp.next is None:
            temp.next = Node(value, exp)

        elif temp.next.exp == exp:
            temp.next.value += value

        else:
            node_temp = Node(value, exp)
            node_temp.next = temp.next
            temp.next = node_temp

    def print(self):
        temp = self.head
        while temp:
            print("{}*x^{}".format(temp.value, temp.exp), end = " ")
            temp = temp.next
            if temp:
                print("+", end = " ")



def function():
    link_list = Formulation()
    formulation1 = input().split()[0::2]
    formulation2 = input().split()[0::2]

    for i in formulation1:
        val, exp = map(int, i.split('*x^'))
        link_list.insert(val, exp)
    for i in formulation2:
        val, exp = map(int, i.split('*x^'))
        link_list.insert(val, exp)

    link_list.print()
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        function()
