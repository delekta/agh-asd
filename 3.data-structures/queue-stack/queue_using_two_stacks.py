# Queue using two stacks


class Stack:
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


class Queue:
    def __init__(self, length):
        self.s1 = Stack(length)
        self.s2 = Stack(length)

    def put(self, element):
        self.s1.push(element)

    def get(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()


n = 10
Q = Queue(10)
for i in range(5):
    el = input("Enter element to put in queue: ")
    Q.put(el)

for i in range(5):
    el = Q.get()
    print(el)


