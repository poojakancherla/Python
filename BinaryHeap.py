class BinaryHeap:
    def __init__(self):
        # Starts with a list consisting of 0 which is not part of the heap
        self.heapList = [0]
        self.currSize = 0

    def insert(self, k):
        # Append the new element
        self.heapList.append(k)
        # Increase the size by 1
        self.currSize = self.currSize + 1
        # Move the element towards the root until it satisfies the heap property. The new element gets appended at the last last index
        siftUp(self.currSize)

    def siftUp(self, i):
        # i // 2 is the index of the root, upto which we need to check for heap property
        while i // 2 > 0:
            # comparing the new element with its parent and swapping if child < parent
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = temp
            i = i // 2

    def delMin(self):
        # Root element is the smallest. So need to return it
        min = self.heaplist[1]
        # Replacing the last element in the root and then sifting it down until the heap property satisfies
        self.heapList[1] = self.heapList[self.currSize]
        self.heapList.pop()
        self.currSize = self.currSize - 1
        siftDown(1)
        return min

    def siftDown(self, i):
        # traverse until the last but one level
        while i * 2 <= self.currSize:
            # minChild helps in deciding between the left and right element with which we need to swap
            minChild = self.minChild(i)
            # swap with the minChild
            if self.heapList[i] > self.heapList[minChild]:
                temp = self.heapList[minChild]
                self.heapList[minChild] = self.heapList[i]
                self.heapList[i] = temp
            i = minChild

    def minChild(self, i):
        # if only left child is present
        if 2 * i + 1 > self.currSize:
            return 2 * i
        else:
            # Compare between the left and right children
            if self.heapList[2 * i] < self.heapList[2 * i + 1]:
                return 2 * i
            else:
                return 2 *i + 1

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currSize = len(alist)
        # The list starts with a 0, which is not part of the heap but is included for integer calculations
        self.heapList = [0] + alist
        # After building the heap from the list, we need  to modify the tree in order to maintain heap property
        while i > 0:
            self.siftDown(i)
            i = i - 1
