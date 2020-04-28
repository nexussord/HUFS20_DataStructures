class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __len__(self):
        return self.size

    def insertAfter(self, a, key):
        new_node = Node(key)
        current = self.head
        while current.key != a:
            temp = current
            current = current.next
            current.prev = temp
        new_node.next = current.next
        new_node.prev = current
        self.head.next = new_node
        self.head.next.prev = new_node
        self.size += 1

    def pushBack(self, key):
        tail = self.head
        for i in range(len(self)):
            tail = tail.next
        self.insertAfter(tail.key, key)

    def deleteNode(self, x):
        print('deletenode')
        print(x.prev.key, x.key, x.next.key)
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1


def josephus(n, k):
    L = DoublyLinkedList()
    L.head.key = 1
    tail = L.head
    for i in range(1, n):
        i += 1
        new_node = Node(i)
        L.pushBack(new_node.key)
        tail = tail.next
    L.head.prev = tail
    current = L.head

    while len(L) != 1:
        print('for')
        for i in range(k-1):
            print(i, current.key, current.next.key)
            current = current.next
        print('delete' + str(current.key))
        L.deleteNode(current)
        current = current.next

    print(current.key)


a, b = map(int, input().split())
josephus(a, b)

