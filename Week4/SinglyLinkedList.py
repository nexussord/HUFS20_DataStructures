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
        s = ""
        v = self.head
        while v:
            s += str(v.key) + " -> "
            v = v.next
        s += "None"
        return s

    def __len__(self):  # len(L): 리스트 L의 size 리턴
        return self.size

    def __iter__(self):
        v = self.head
        while v:
            yield v
            v = v.next

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
        key = value = None
        if len(self) > 0:
            key = self.head.key
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
        return key, value

    def popBack(self):
        if self.size == 0:
            return None, None
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
            return key, value

    def search(self, key):
        for v in self:
            if v.key == key:
                return v

        return None

    def remove(self, key):
        v = L.search(key)
        if self.size == 0:
            return None, None
        else:
            previous = None
            current = self.head
            while current != v:
                previous = current
                current = current.next
            rem = current
            key = rem.key
            value = rem.value
            if current == self.head:
                self.head = current.next
            else:
                previous.next = current.next
            self.size -= 1
            return key, value



    def size(self):
        return self.size


L = SinglyLinkedList()
L.pushBack(10)
L.pushBack(20)
L.pushBack(40)
print(L)
L.remove(40)
print(L)