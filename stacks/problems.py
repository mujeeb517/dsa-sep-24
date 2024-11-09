def is_opening(c):
    return c == '[' or c == '(' or c == '{'


def valid_parentheses(s):
    stack = []
    for c in s:
        if is_opening(c):
            stack.append(c)
        else:
            if not stack:
                return False
            top = stack.pop()
            if top == '(' and c != ')':
                return False
            if top == '[' and c != ']':
                return False
            if top == '{' and c != '}':
                return False

    return len(stack) == 0


'''
aabbac


c
a
'''


def remove_adjacent_duplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)


def warm_temperature(temps):
    res = []
    stack = []

    for i in temps[::-1]:
        if stack and temps[stack[-1]] <= temps[i]:
            stack.pop()
        
        res[i] = stack.top()-i if stack else 0
       
    return res
