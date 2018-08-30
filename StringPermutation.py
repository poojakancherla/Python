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

print(permute('abc'))
