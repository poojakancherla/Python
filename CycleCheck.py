from nose.tools import assert_equal

class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

# Creating a SinglyLinkedList with a cycle

a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c = SinglyLinkedListNode(3)
a.next_node = b
b.next_node = c
c.next_node = a # This is the cycle

#Creating a SinglyLinkedList without any cycles

x = SinglyLinkedListNode(1)
y = SinglyLinkedListNode(2)
z = SinglyLinkedListNode(3)

x.next_node = y
y.next_node = z

#  To check if there is a cycle, we can take two markers starting at the same node. One pointer will be faster than the other, such that
# if there is a cycle, the faster marker will meet the slower marker. If it doesn't have a cycle, the two markers will never meet

def cycle_check(node):
    marker1 = node
    marker2 = node
    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker1 == marker2:
            return True
    return False

class TestCycleCheck(object):

    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)

        print("ALL TEST CASES PASSED")

# Run Tests

t = TestCycleCheck()
t.test(cycle_check)
