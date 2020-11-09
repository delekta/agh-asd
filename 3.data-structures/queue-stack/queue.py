# Implementation of queue using Linked List
class Node:
    def __init__(self):
        self.next = None
        self.val = None


class QueueL:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def put(self, val):
        new = Node()
        new.val = val
        self.tail.next = new
        self.tail = self.tail.next

    def get(self):
        # if we get the only one element
        if self.head.next is self.tail:
            self.tail = self.head

        temp = self.head.next
        self.head.next = temp.next
        return temp.val

    def top(self):
        return self.head.next.val

    def is_empty(self):
        return self.head.next is None


# Implementation of queue using Array
class QueueA:
    def __init__(self, length):
        self.arr = [None] * length
        self.length = length
        self.head = 0
        self.size = 0

    def put(self, val):
        idx = (self.head + self.size) % self.length
        self.size += 1
        self.arr[idx] = val

    def get(self):
        res = self.arr[self.head]
        self.head = (self.head + 1) % self.length
        self.size -= 1
        return res

    def top(self):
        return self.arr[self.head]

    def is_empty(self):
        return self.size == 0


length = 5
L = QueueL()
A = QueueA(length)

for _ in range(5):
    el = input("Enter value:")
    A.put(el)
    L.put(el)

# Showing that queue is crawl (% length)
print(A.get())
A.put(6)
print(A.arr)

for _ in range(5):
    print(A.get())

print("\n")

for _ in range(5):
    print(L.get())





