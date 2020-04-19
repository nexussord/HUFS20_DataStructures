class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # head 노드를 저장함
        self.size = 0  # 리스트의 노드 개수를 저장함

    def __str__(self):  # print() 출력용 문자열 리턴
        return str(self.key)

    def __len__(self):  # len(L): 리스트 L의 size 리턴
        return self.size

    def __iter__(self):
        v = self.head
        while v:
            yield v
            v = v.next

    def printList(self):  # 변경없이 사용할 것!
        v = self.head
        while (v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key, value=None):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node  # head 노드가 바뀜
        self.size += 1

    def pushBack(self, key, value=None):
        new_node = Node(key, value)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        if self.size == 0:
            return None
        key = value = None
        if len(self) > 0:
            key = self.head.key
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
        return key

    def popBack(self):
        if self.size == 0:
            return None
        else:
            previous = None
            current = self.head
            while current.next is not None:
                previous = current
                current = current.next
            # if there is only one node inside the list, it will be both head and tail.
            # in such case, deleting tail will make list empty, so should be edited as head = None
            tail = current
            key = tail.key
            value = tail.value
            if self.head == tail:  # if previous == None:
                self.head = None
            else:
                previous.next = tail.next  # previous becomes new tail
            self.size -= 1
            return key

    def search(self, key):
        ans = None
        for v in self:
            if v.key == key:
                ans = key
                break

        return ans

    def remove(self, x):
        v = L.search(x)
        if v == self.head:
            self.popFront()
            self.size -= 1
            return True
        elif v is None:
            return False
        else:
            previous = None
            current = self.head
            while current is not v:
                previous = current
                current = current.next
            print(v, previous, current, current.next)
            previous.next = current.next
            self.size -= 1
            return True

    def size(self):
        return self.size


L = SinglyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == "pushFront":
        L.pushFront(int(cmd[1]))
        print(int(cmd[1]), "is pushed at front.")
    elif cmd[0] == "pushBack":
        L.pushBack(int(cmd[1]))
        print(int(cmd[1]), "is pushed at back.")
    elif cmd[0] == "popFront":
        x = L.popFront()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from front.")
    elif cmd[0] == "popBack":
        x = L.popBack()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from back.")
    elif cmd[0] == "search":
        x = L.search(int(cmd[1]))
        if x == None:
            print(int(cmd[1]), "is not found!")
        else:
            print(int(cmd[1]), "is found!")
    elif cmd[0] == "remove":
        x = L.search(int(cmd[1]))
        if L.remove(x):
            print(x.key, "is removed.")
        else:
            print("Key is not removed for some reason.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")
