class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

s = Stack()
s.push(6)
print(s.peek())
