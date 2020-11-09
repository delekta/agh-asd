# Write a function that takes two lists, each of which is sorted in increasing
# order, and merges the two together into one list which is in decreasing order
# and return it. In other words, mergetwo sorted linked list from their ends
# Input: {1, 3, 5} and {2, 6, 7, 10}
# Output: {10, 7, 6, 5, 3, 2, 1}

class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
#   adding to front
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

def Merge(a, b):
    result = LinkedList()
    while a != None and b != None:
        if a.data < b.data:
            result.insert(a.data)
            a = a.next
        else:
            result.insert(b.data)
            b = b.next
    while a != None:
        result.insert(a.data)
        a = a.next
    while b != None:
        result.insert(b.data)
        b = b.next
    return result

li1 = LinkedList()
print("Make first list: ")
while True:
    print("Jesli chcesz zakonczyc wcisnij \"-1\"")
    val = int(input("Podaj wartosc:"))
    if val == -1:
        break
    li1.insert(val)
    li1.printList()
print("Make second list: ")
li2 = LinkedList()

while True:
    print("Jesli chcesz zakonczyc wcisnij \"-1\"")
    val = int(input("Podaj wartosc:"))
    if val == -1:
        break
    li2.insert(val)
    li2.printList()

result = Merge(li1.head, li2.head)
result.printList()



