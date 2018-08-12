def uni_char(s):
    d = {}
    for i in s:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

##### Alternate Solution

# def uni_char(s):
#     return len(set(s)) == len(s)



print(uni_char('abccdef'))
