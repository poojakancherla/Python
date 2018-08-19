def match(string):
    lookup = {'(': ')', '[':']', '{':'}'}
    stack = []
    for element in string:
        if element in lookup:
            stack.append(element)
        elif len(stack) == 0 or element != lookup[stack.pop()]:
            return False
    return len(stack) == 0


print(match('(){}['))
