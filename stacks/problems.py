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
    n = len(temps)
    res = [0]*n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and temps[stack[-1]] <= temps[i]:
            stack.pop()

        res[i] = stack[-1]-i if stack else 0

        stack.append(i)

    return res


def is_operator(c):
    return c == '+' or c == '-' or c == '*' or c == '/'


def calculate(op1, op2, op):
    if op == '+':
        return op1+op2
    if op == '-':
        return op1-op2
    if op == '*':
        return op1*op2
    if op == '/':
        return op1/op2


def evaluate_prefix(s):
    n = len(s)
    stack = []

    for c in s[::-1]:
        if (is_operator(c)):
            op1 = stack.pop()
            op2 = stack.pop()
            res = calculate(int(op1), int(op2), c)
            stack.append(res)
        else:
            stack.append(c)

    return stack[-1]

# +, *


def has_higher_prcedence(c, top):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    return precedence[top] >= precedence[c]


def infix_to_postfix(s):
    res = []
    stack = []
    for c in s:
        if (is_operator(c)):
            while stack and has_higher_prcedence(c, stack[-1]):
                res.append(stack.pop())
            stack.append(c)
        else:
            res.append(c)

    while stack:
        res.append(stack.pop())

    return ''.join(res)
