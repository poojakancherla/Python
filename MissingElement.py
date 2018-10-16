def find(array1, array2):
    d = {}
    for i in array1:
        d[i] = 1
    for i in array2:
        if d[i] == 1:
            del d[i]
    for key in d:
        print(key)

find([1,2,3,4,5,6,7], [3,7,2,1,4,6])


# In case duplicates are allowed

def find2(arr1, arr2):
    d = {}
    for i in arr1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in arr2:
        if d[i] > 1:
            d[i] -= 1
        elif d[i] == 1:
            del d[i]
    for key in d:
        print(key)
find2([4, 1, 3, 4], [3, 4, 4])
