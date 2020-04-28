class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def splice(self, a, b, x):  # cut [a..b] after x
        if a == None or b == None or x == None:
            return
        # 1. [a..b] 구간을 잘라내기
        a.prev.next = b.next
        b.next.prev = a.prev

        # 2. [a..b]를 x 다음에 삽입하기
        x.next.prev = b
        b.next = x.next
        a.prev = x
        x.next = a

    def moveAfter(self, a, x):
        self.splice(a, a, x)

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertAfter(self, a, key):
        new_node = Node(key)
        self.moveAfter(new_node, a)

    def insertBefore(self, a, key):
        new_node = Node(key)
        self.moveBefore(new_node, a)

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def deleteNode(self, x):  # delete x
        if x == None or x == self.head:
            return
        # 노드 x를 리스트에서 분리해내기
        x.prev.next, x.next.prev = x.next, x.prev
        del x

    def popFront(self):
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        return key

    def popBack(self):
        if self.head.next == self.head:
            return None
        key = self.head.prev.key
        self.deleteNode(self.head.prev)
        return key

    def printList(self):
        v = self.head.next
        if self.head.next == self.head:
            print("h")
        else:
            print("h ->", end=" ")
            while v.key != self.head.key:
                print(v.key, "->", end=" ")
                v = v.next
            print("h")

    def isEmpty(self):
        if self.head.next is self.head:
            return True
        else:
            return False

    def first(self):
        if self.head.next is self.head:
            return None
        else:
            return self.head.next

    def last(self):
        if self.head.next is self.head:
            return None
        else:
            v = self.head.next
            while v.next.key != self.head.key:
                v = v.next
            return v.key

    def search(self, key):
        current = self.head
        while current.next != self.head:
            current = current.next
            if current.key == key:
                return current
        return None

L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")