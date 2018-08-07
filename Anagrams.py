s1 = 'aa'
s2 = 'a a'

def anagram(s1, s2):
    d = {}
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return 'Not Anagrams'
    for i in s1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in s2:
        if i in d:
            d[i] -= 1
        else:
            return 'Not Anagrams'

    for k in d:
        if d[k] != 0:
            return 'Not Anagrams'
    else:
        return 'Anagrams'


print(anagram(s1, s2))
