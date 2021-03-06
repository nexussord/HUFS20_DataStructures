class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __len__(self):
        return self.size

    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        # splice [a...b]
        a.prev.next = b.next
        b.next.prev = a.prev
        # insert [a...b] after x
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
        self.size += 1

    def insertBefore(self, a, key): # 4 1
        new_node = Node(key)
        self.moveBefore(new_node, a)
        self.size += 1

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def deleteNode(self, x):
        if x == None or x == self.head:
            return None
        x.prev.next = x.next
        x.next.prev = x.prev
        del x
        self.size -= 1

    def popFront(self):
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        self.size -= 1
        return key

    def popBack(self):
        if self.head.next.key == self.head.key:
            return None
        tail = self.head
        for i in range(len(self)):
            tail = tail.next
        key = tail.key
        self.deleteNode(tail)
        self.size -= 1
        return key

    def search(self, key):
        current = self.head
        while current.next != self.head:
            current = current.next
            if current.key == key:
                return current
        return None

    def isEmpty(self):
        if self.head.next is self.head:
            return True
        else:
            return False

    def first(self):
        if self.head.next is self.head:
            return None
        else:
            return self.head

    def last(self):
        if self.head.next is self.head:
            return None
        else:
            return self.head.prev

    def join(self, list):
        temp = DoublyLinkedList()
        temp.head.next = temp.head
        temp.head.prev = temp.head
        for i in range(list):
            temp.pushBack(list[i])
        self.splice(temp.head, temp.head.prev, self.head.prev)

    def split(self, x):
        temp = DoublyLinkedList()
        temp.head.next = temp.head
        temp.head.prev = temp.head
        self.splice(self.x, self.head.prev, temp.head)

    def printList(self):
        v = self.head.next
        if self.head.next == self.head:
            print("h")
        else:
            print("h ->", end=" ")
            for i in range(len(self)):
                print(v.key, "->", end=" ")
                v = v.next
            print("h")


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


