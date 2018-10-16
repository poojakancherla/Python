def compress(s):
    if len(s) == 0:
        return ''
    else:
        s_compress = ""
        curr = s[0]
        count = 1
        for i in s[1:]:
            if i == curr:
                count += 1

            else:
                s_compress += curr + str(count)
                count = 1
                curr = i
    return s_compress +curr + str(count)

print(compress("My name is Pooja"))
