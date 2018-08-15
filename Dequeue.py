class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_rear(self, item):
        return self.items.insert(0, item)

    def add_front(self, item):
        return self.items.append(item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


deq = Deque()

deq.add_rear(6)
deq.add_front(7)
deq.remove_rear()
print(deq.is_empty())
print(deq.size())
print(deq.items)
