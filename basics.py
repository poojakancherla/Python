import random
import sys
import os


############## LISTS #######################

# s1 = "Shine bright like a diamond"
# s2 = "Sunshine"
#
# print("%s and %s %s" %(s1, "everyday", s2) )
#
# print("balle balle ", end = "")
# print("shava shava")
#
# list1 = ['a', 'b', 'c', 'd']
# list2 = ['e', 'f', 'g', 'h']
#
# list3 = [list1, list2]
# print(list3)
#
# list4 = list1 + list2
# print(list4)
#
# list4.append('i')
# print(list4)
#
# list4.insert(1, 'd')
# print(list4)
#
# print(len(list4))
#
# list4.remove('a')
# print(list4)
#
# list4.sort()
# print(list4)
#
# del list4[2]
# print(list4)
#
# print(max(list4))


############# DICTIONARIES ######################


# fruits = {"mango" : 100, 'apple': 200, 'banana':300, 'grapes':400, 'berry':500}
#
# print(fruits['banana'])
#
# del fruits['berry']
#
# fruits['grapes'] = 700
#
# print(len(fruits))
#
# print(fruits)


########### FILE I/O #########################

# test_file = open("test.txt", "r+")
# line = test_file.read()
# print(line)
# os.remove("test.txt")

# with open("test.txt") as f:
#     for line in f:
#         print(line)


######## OBJECTS ###########################
#
class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0
