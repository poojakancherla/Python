# Import the heap functions from python library

import heapq
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time

# This program is for Min Heap
class BinaryHeap:

    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    # Inserts a new key 'k'
    def insertKey(self, k):
        heapq.heappush(self.heap, k)

    # Decrease value of key at index 'i' to new_val
    # It is assumed that newVal is smaller than heap[i]
    def reduceKey(self, i , newVal):
        self.heap[i] = newVal
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[self.parent(i)], self.heap[i] = (self.heap[i], self.heap[self.parent(i)])

    # Method to remove minium element from Binary heap
    def extractMin(self):
        return heapq.heappop(self.heap)

    # This functon deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.reduceKey(i, float("-infinity"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]


# Driver program to test above function
heapObj = BinaryHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.deleteKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

print(heapObj.extractMin())
print (heapObj.getMin())
heapObj.reduceKey(2, 1)
print(heapObj.getMin())
