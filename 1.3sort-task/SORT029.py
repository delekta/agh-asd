# Zadanie 8
# Dana jest klasa :
# class Node:
# val = 0
# next = None
# reprezentująca węzeł jednokierunkowego łańcucha odsyłaczowego, w którym wartości val
# poszczególnych węzłów zostały wygenerowane zgodnie z rozkładem jednostajnym na przedziale [a, b].
# Napisz procedurę sort(first), która sortuje taką listę. Funkcja powinna być jak najszybsza.
# Nie dziala 26.03.2020


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def link(self, link):
        link.next = None
        link = self.head
        self.head = link

    def printList(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

# nie dziala do konca 26.03.2020
def insertion_sort_bucket(head, last):
    # glupi kompilator
    first = head
    res = LinkedList()
    while first is not None:
        curr = first
        prev = None
        prev_max = None
        curr_max = curr
        max = -float('inf')
        while curr is not None:
            if curr.val > max:
                max = curr.val
                prev_max = prev
                curr_max = curr
            prev = curr
            curr = curr.next

        if prev_max is None:
            first = first.next
            res.link(curr_max)
        else:
            prev_max.next = curr_max.next
            res.link(curr_max)
        if res.head.next is None:
            last = res
    head = res

# dziwne listy w python
def last_node(first):
    curr = first
    while curr.next is not None:
        curr = curr.next
    return curr


# Defining function which will merge two linked lists
def mergeLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp = l1
        temp.next = mergeLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeLists(l1, l2.next)
    return temp


# Defining function which will sort the linked list using mergeSort
def mergeSort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divideLists(head)
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    head = mergeLists(l1, l2)
    return head


# Defining function which will divide a linked list into two equal linked lists
def divideLists(head):
    slow = head  # slow is a pointer to reach the mid of linked list
    fast = head  # fast is a pointer to reach the end of the linked list
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None
    return head, mid

def bucket_list_sort(head, n, a, b):
    normal = b - a
    first = []
    last = []
    for i in range(n):
        first.append(None)
        last.append(None)

    # dividing in buckets
    while head is not None:
        idx = int((((head.val - a) / normal) * (n - 1)))
        if first[idx] is None:
            first[idx] = head
            last[idx] = first[idx]
        else:
            last[idx].next = head
            last[idx] = last[idx].next

        head = head.next
        last[idx].next = None

    res = None
    for i in range(n - 1, -1, -1):
        mergeSort(first[i])
        last[i] = last_node(first[i])
        last[i].next = res
        res = first[i]

    head = res

li = LinkedList()

li.insert(16)
li.insert(18)
li.insert(21)
li.insert(19)
li.insert(20)
li.insert(15)
li.insert(25)
li.insert(23)
li.insert(24)
li.printList()
n = 9
a = 15
b = 25
bucket_list_sort(li.head, n, a, b)
li.printList()
