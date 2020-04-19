class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
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

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node  # head 노드가 바뀜
        self.size += 1

    def pushBack(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        key =  None
        if len(self) == 0:
            return None
        elif len(self) > 0:
            key = self.head.key
            self.head = self.head.next
            self.size -= 1
        return key

    # head 노드의 값 리턴. empty list이면 None 리턴

    def popBack(self):
        if len(self) == 0:
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
            if self.head == tail:  # if previous == None:
                self.head = None
            else:
                previous.next = tail.next  # previous becomes new tail
            self.size -= 1
            return key

    # tail 노드의 값 리턴. empty list이면 None 리턴

    def search(self, key):
        for v in self:
            if v.key == key:
                return v

        return None

    # key 값을 저장된 노드 리턴. 없으면 None 리턴

    def remove(self, x):  # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴 # x는 key 값이 아니라 노드임에 유의!
        if x is None:
            return False
        else:
            v = self.head
            prev = None
            tail = v
            if int(str(v)) == int(str(x)):
                self.popFront()
                return True
            while v:
                prev = tail
                tail = tail.next
                if int(str(tail)) == int(str(x)):
                    if v.next is not None:
                        prev.next = tail.next
                        del v
                        self.size -= 1
                        return True
                    else:
                        self.popBack()
                        return True
                v = v.next

    # def remove(self, x):
    #     if self.size == 0:
    #         return False
    #     else:
    #         previous = None
    #         current = self.head
    #         while current.next is not None:
    #             if current == x.key:
    #                 previous.next = current.next
    #                 self.size -= 1
    #                 return True
    #             previous = current
    #             current = current.next
    #         return False

    def reverse(self):
        N = SinglyLinkedList()
        v = self.head
        for i in range(len(self)):
            N.pushFront(v)
            v = v.next
        v = N.head
        for i in range(len(self)):
            L.pushBack(v)
            v = v.next
            L.popFront()
        pass

    def findMax(self): # self가 empty이면 None, 아니면 max key 리턴
        if len(self) is 0:
            return None
        else:
            max = self.head
            v = self.head
            for i in range(len(self)):
                if int(str(v.key)) >= max:
                    max = int(str(v.key))
                v = v.next
            return max

    def deleteMax(self):
        if len(self) is 0:
            return None
        else:
            max = self.findMax()
            self.remove(max)
            return max
        # self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
        pass

    def insert(self, k, val):
        new_node = Node(val)
        if k >= len(self):
            self.pushBack(val)
        else:
            v = self.head
            prev = None
            current = v
            for i in range(k):
                prev = current
                current = current.next
            prev.next = new_node
            new_node.next = current
        pass

    # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
    def size(self):
        return self.size


# 아래 코드는 수정하지 마세요!
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
    elif cmd[0] == "reverse":
        L.reverse()
    elif cmd[0] == "findMax":
        m = L.findMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key is", m)
    elif cmd[0] == "deleteMax":
        m = L.deleteMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key", m, "is deleted.")
    elif cmd[0] == "insert":
        L.insert(int(cmd[1]), int(cmd[2]))
        print(cmd[2], "is inserted at", cmd[1]+"-th position.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")