# Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
# struct Node{ Node* next;
#              double value; }
# Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę liczb rzeczywistych
# (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na przedziale [0,10) i sortuje jej zawartość
# w kolejności niemalejącej. Funkcja powinna być możliwie jak najszybsza (biorąc pod uwagę warunki zadania).
# Proszę oszacować złożoność zaimplementowanej funkcji.


class Node:
    def __init__(self):
        self.next = None
        self.val = None


class List:
    def __init__(self):
        self.head = Node()
        self.tail = None


def merge(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        temp = list1
        temp.next = merge(list1.next, list2)
    else:
        temp = list2
        temp.next = merge(list1, list2.next)
    return temp


def divide_list(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next

    mid = slow.next
    slow.next = None

    # you must return "head", mid
    return head, mid


# bucket is a linked list
def merge_sort(head):
    if head is None or head.next is None:
        return head
    start, mid = divide_list(head)

    b1 = merge_sort(start)
    b2 = merge_sort(mid)

    return merge(b1, b2)


def add(bucket, node):
    node.next = None
    if bucket.head.next is None:
        bucket.head.next = node
        bucket.tail = node
    else:
        bucket.tail.next = node
        bucket.tail = node


def add_to_the_head(head, node):
    if head is None:
        head = node
    else:
        node = head.next
        head = node

def print_list(L):
    head = L.head.next

    while head:
        print(head.val, end=" ")
        head = head.next
    print("\n")


# length -> length of L(number of node
def bucket_sort(L, length):
    buckets = [List() for _ in range(length)]
    curr = L.head.next
    while curr:
        temp = curr.next

        idx = int((curr.val / 10) * length)
        add(buckets[idx], curr)

        curr = temp

    for bucket in buckets:
        if bucket.head.next is not None:
            bucket.head.next = merge_sort(bucket.head.next)

    result = List()
    for bucket in buckets:
        if bucket.head.next is not None:
            if result.head.next is None:
                # must be bucket.next."next" beacause we dont wont to add watcher to result
                result.head.next = bucket.head.next
                result.tail = bucket.tail
            else:
                # must be bucket.next."next" beacause we dont wont to add watcher to result
                result.tail.next = bucket.head.next
                result.tail = bucket.tail

    return result



L = List()

n1 = Node()
n1.val = 4
n2 = Node()
n2.val = 2
n3 = Node()
n3.val = 9
n4 = Node()
n4.val = 7
n5 = Node()
n5.val = 6
n6 = Node()
n6.val = 8

# we can count it passing list
length = 6

add(L, n1)
add(L, n2)
add(L, n3)
add(L, n4)
add(L, n5)
add(L, n6)

# testing merge_sort
# print_list(L)
# L.head.next = merge_sort(L.head.next)
# print_list(L)

print_list(L)
L = bucket_sort(L, length)
print_list(L)

