class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def reverse(head):
        curr = head
        previous, next = None, None
        while curr:
            next = curr.next_node
            curr.next_node = previous

            previous = curr
            curr = next

        return previous

    def printt(self, a):
        print(89)
# Testing the Solution

# Create a list of 4 nodes
a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c = SinglyLinkedListNode(3)
d = SinglyLinkedListNode(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next_node = b
b.next_node = c
c.next_node = d
print (a.next_node.value)
print (b.next_node.value)
print (c.next_node.value)


SinglyLinkedListNode.reverse(a)
f = SinglyLinkedListNode(19)
f.printt(100)
# Check if the Linked List is reversed
print (d.next_node.value)
print (c.next_node.value)
print (b.next_node.value)
