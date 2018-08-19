class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c = SinglyLinkedListNode(3)

a.next_node = b
b.next_node = c

print(a.value)
print(a.next_node)
print(b.value)
