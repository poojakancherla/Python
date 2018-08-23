class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def nth_to_last_node(self, n, head):
        curr = head
        last, nth_node = None, None
        counter = 0
        #  Finding the last element and size of the list
        while curr:
            last = curr.next_node
            curr = last
            counter += 1
        #  Using the size, traversing to the nth node
        for i in range(counter - n):
            nth_node = head.next_node
            head = nth_node


        return nth_node.value



# Testing
a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)
e = LinkedListNode(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e


obj = LinkedListNode(object)
print(obj.nth_to_last_node(3, a))
