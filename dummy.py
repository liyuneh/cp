class Uniquestack:
    def __init__(self):
        self.stack = []
        self.values = set()
    def insert(self, value):
        if value not in self.values:
            self.stack.append(value)
            self.values.add(value)
            return f"{value} inserted successfully."
        return f"{value} already existed inthe stack."
    def delete(self):
        if self.stack:
            value = self.stack.pop()
            self.values.remove(value)
            return f"{value} removed successfully. "
        return "stack is empty."
    def search(self, value):
        if value in self.values:
            return f"{value} found."
        return f"{value} not found in the stack."
    def delete_at_index(self, index):
        if 0 <= index < len(self.stack):
            value = self.stack.pop(index)
            self.values.remove(value)
            return f"{value} removed successfully at index {index}. "
        return "index out of range."
stack = Uniquestack()
print(stack.insert(10))  
print(stack.insert(20)) 
print(stack.insert(30))  
print(stack.insert(10))  
print(stack.search(10))  
print(stack.delete())
print(stack.search(10))
print(stack.delete_at_index(0))
print(stack.delete_at_index(5))  