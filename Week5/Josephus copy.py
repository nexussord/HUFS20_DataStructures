class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        self.insert_at_end(node)

    def get_node(self, index, start):
        if self.head is None:
            return None
        current = start
        for i in range(index):
            current = current.next
        return current

    def get_prev_node(self, ref_node):
        if self.head is None:
            return None
        current = self.head
        while current.next != ref_node:
            current = current.next
        return current

    def insert_after(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node

    def insert_before(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)

    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            self.insert_before(self.head, new_node)

    def remove(self, node):
        if self.head.next == self.head:
            self.head = None
        else:
            prev_node = self.get_prev_node(node)
            prev_node.next = node.next
            if self.head == node:
                self.head = node.next


def has_one_node(temp):
    if temp.head.next == temp.head:
        return True
    else:
        return False


def ans(temp, k):
    if temp.head is None:
        return None
    start = temp.head
    while not has_one_node(temp):
        to_remove = temp.get_node(k - 1, start)
        start = to_remove.next
        temp.remove(to_remove)
    return temp.head.data


L = DoublyLinkedList()
n, k = map(int, input().split())
for i in range(1, n + 1):
    L.append(i)

print(ans(L, k))
