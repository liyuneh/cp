class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def Print(self):
        for item in reversed(self.items):
            print(item)
s = Stack()
print(s.is_empty())
s.push(3)
s.push(True)
s.push(5)
s.push(10.5)
print(s.peek())
print(s.size())
s.pop()

s.Print()
print(s.peek())
