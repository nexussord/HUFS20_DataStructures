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

postfix = input()
answer = compute_postfix(postfix)
print(format(answer, ".4f"))