#  Problem 1
# def rec_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + rec_sum(n-1)
# print(rec_sum(4))


# Problem 2
# def sum_func(n):
#     if n < 10:
#         return n
#     else:
#         return (n % 10 + sum_func(n // 10))
# print(sum_func(4321))

# Problem 3
def word_split(phrase, list_of_words, output = None):
    if output == None:
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output

print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
