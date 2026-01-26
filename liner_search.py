class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def length(self):
        cur = self.head
        total = 0
        while cur:
            cur = cur.next
            total += 1
        return total - 1

    def display(self):
        element = []
        cur = self.head
        while cur:
            if cur.val is not None:
                element.append(cur.val)
            cur = cur.next
        print(element)

    def erase(self, index):
        if index >= self.length():
            return "Error: index out of range"
        cur = self.head
        count = 0
        while cur.next:
            last = cur.next
            if count == index:
                cur.next = last.next
                return
            cur = cur.next
            count += 1


my_list = Linkedlist()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)

my_list.display()

my_list.erase(3)

my_list.display()
