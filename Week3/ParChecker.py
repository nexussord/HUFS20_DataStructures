class Stack:
    def __init__(self):
        self.items = []

    def push(self,val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def len(self):
        return len(self.items)

def parchecker(parseq):
    s = Stack()
    for symbol in parseq:
        if symbol is "(":
            s.push(symbol)
        elif symbol is ")":
            if s.len() is 0:
                return False
            else:
                s.pop()
    if s.len() is 0:
        return True
    else:
        return False

parseq = input("Type in String : ")
if parchecker(parseq) is True:
    print(True)
else:
    print(False)

