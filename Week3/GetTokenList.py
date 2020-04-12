# 3+ 2* 4/(6- 1)
def infix_to_postfix(token_list):

    return token_list

def get_token_list(expr):
    expr = expr.replace(" ", "")
    print(expr)
    temp = []
    tokens = ''
    for i in expr :
        if i in '+-*/()':
            temp.append(tokens)
            tokens = ''
            temp.append(i)
        else :
            tokens+=i

    return temp

expr = input()
print(infix_to_postfix(get_token_list(expr)))