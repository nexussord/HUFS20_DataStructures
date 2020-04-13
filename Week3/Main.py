class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def len(self):
        return len(self.items)

    def isEmpty(self):
        return self.len() == 0

def get_token_list(expr):
    expr = expr.replace(" ", "")
    # print(expr)
    temp = []
    tokens = ''
    for i in expr:
        if i in '+-*/()':
            temp.append(tokens)
            tokens = ''
            temp.append(i)
        else:
            tokens += i

    return temp

def infix_to_postfix(token_list):
    opstack = Stack()
    outstack = []
    token_list.remove('')

# 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
            opstack.push(token)

        elif token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()

        elif token in '+-/*^':
            if opstack.isEmpty():
                opstack.push(token)
            elif prec[token] > prec[opstack.top()]:
                opstack.push(token)
            else:
                while prec[opstack.top()] >= prec[token]:
                    outstack.append(opstack.pop())
                    if opstack.isEmpty(): break
                opstack.push(token)
        else:
            outstack.append(token)
    while opstack.len() is not 0:
        outstack.append(opstack.pop())
    return " ".join(outstack)


def calculate_postfix(a, b, token):
    if token is '+':
        return b + a
    elif token is '-':
        return b - a
    elif token is '*':
        return b * a
    elif token is '/':
        return b / a
    elif token is '^':
        return b ^ a


def compute_postfix(postfix):
    s = Stack()
    token_list = postfix.split(' ')
    for token in token_list:
        if token in '+-*/^':
            a = float(s.pop())
            b = float(s.pop())
            result = calculate_postfix(a, b, token)
            s.push(result)
        else:
            s.push(token)
    return s.pop()

# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)