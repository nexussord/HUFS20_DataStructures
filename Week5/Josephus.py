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

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertBefore(self, a, key):
        new_node = Node(key)
        self.moveBefore(new_node, a)

    def pushBack(self, key):
        self.insertBefore(self.head, key)
        self.size += 1

    def deleteNode(self, x):  # delete x
        if x == None or x == self.head:
            return
        # 노드 x를 리스트에서 분리해내기
        x.prev.next, x.next.prev = x.next, x.prev
        del x
        self.size -= 1

def joseephus(n, k):
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

    while len(L) > 1:
        print('for')
        for i in range(k - 1):
            print(i, current.key, current.next.key)
            current = current.next
        print('delete' + str(current.key))
        L.deleteNode(current)
        current = current.next
    #
    current = current.next
    # print('delete' + str(current.key))
    # L.deleteNode(current)
    print(current.key)


def josephus(n, k):
    if (n == 1):
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


a, b = map(int, input().split())
print(josephus(a, b))

