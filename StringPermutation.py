def permute(s):
    output = []

    if len(s) == 1:
        output = [s]
    else:
        for i in range(len(s)):
            s1 = s.replace(s[i], '')

            for perm in permute(s1):

                output += [s[i] + perm]
    return output

# print(permute('abc'))

def rem(s, i):
    s1 = list(s)
    s1.remove(i)
    s2 = "".join(s1)


def permute2(s):
    output = []
    if len(s) == 1:
        return s
    else:
        for i in s:
            output += i + permute2(rem(s, i))

print(permute2("abc"))
