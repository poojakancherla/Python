import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getItem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('k is out of bounds')
        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap) # Making a New Array with double the capacity
        for k in range(self.n):
            B[k] = self.A[k] # Copying the elements to the New Array
        self.A = B  # Renaming the New Array with the Original Name
        self.capacity = new_cap # updating the capacity

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

        
###### Testing ########
arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append('cat')
print(arr.__getItem__(1))
