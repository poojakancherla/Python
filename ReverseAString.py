#  Reverse a string using recursion

def reverse(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

print(reverse('hello world'))
