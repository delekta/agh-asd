# Implementation of stack using Array
class StackA:
    def __init__(self, length):
        self.arr = [None] * length
        self.length = length
        self.size = 0

    def push(self, element):
        self.arr[self.size] = element
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.arr[self.size]

    def top(self):
        return self.arr[self.size - 1]

    def is_empty(self):
        return self.size == 0


# Implementation of stack using Linked List
class Node:
    def __init__(self):
        self.next = None
        self.val = None


class StackL:
    def __init__(self):
        self.top = Node()

    def push(self, val):
        new = Node()
        new.val = val
        new.next = self.top.next
        self.top.next = new

    def pop(self):
        temp = self.top.next
        self.top.next = temp.next
        return temp.val

    def top(self):
        return self.top.next

    def is_empty(self):
        return self.top.next is None


length = 10
A = StackA(length)
L = StackL()
for _ in range(5):
    el = input("Enter value:")
    A.push(el)
    L.push(el)

for _ in range(5):
    print(A.pop())
    print(L.pop())
