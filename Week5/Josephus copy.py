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
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        self.head.next = new_node
        self.head.prev = new_node
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


def josephus(c, k):
    L = DoublyLinkedList()
    ls = []
    tail = L.head
    for i in range(1, c+1):
        new_node = Node(i)
        ls.append(i)
        tail = tail.next
    k -= 1 # pop automatically skips the dead guy
    idx = k
    while len(ls) > 1:
        ls.pop(idx) # kill prisoner at idx
        idx = (idx + k) % len(ls)
    print(ls[0])


a, b = map(int, input().split())
josephus(a, b)

