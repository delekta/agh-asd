# Lista L jest dostępna w postaci krotki (firs,last) zawierającej wskazania na pierwszy
# i ostatni element listy.
# Proszę zaimplementować funkcję:
# def QuickSort( L )
# sortującą listę L i zwracającą posortowaną listę także w postaci krotki (first,last)


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class List:
    def __init__(self):
        self.head = None
        self.tail = None


def merge_list(list_of_list):
    result = List()
    for lista in list_of_list:
        if lista.head is not None:
            if result.head is None:
                result.head = lista.head
                result.tail = lista.tail
            else:
                # must be result.tail.next not result.tail
                result.tail.next = lista.head
                result.tail = lista.tail

    return result


def is_empty(L):
    return L.head is None


def has_one_enemy(L):
    return L.head is L.tail


def add(node, lista):
    node.next = None
    if lista.head is None:
        lista.head = node
        lista.tail = node
    else:
        lista.tail.next = node
        lista.tail = node


def quicker_sort(L):
    if is_empty(L) or has_one_enemy(L):
        return L

    curr = L.head

    smaller = List()
    equal = List()
    greater = List()
    pivot = L.tail.val

    while curr:
        # important
        temp = curr.next
        if curr.val < pivot:
            add(curr, smaller)
        elif curr.val == pivot:
            add(curr, equal)
        else:
            add(curr, greater)
        curr = temp

    return merge_list([quicker_sort(smaller), equal, quicker_sort(greater)])


def print_list(L):
    head = L.head

    while head:
        print(head.val, end =" ")
        head = head.next


L = List()

n1 = Node(4)
n2 = Node(2)
n3 = Node(9)
n4 = Node(7)
n5 = Node(6)
n6 = Node(8)

add(n1, L)
add(n2, L)
add(n3, L)
add(n4, L)
add(n5, L)
add(n6, L)

# print_list(L)
print("Before:", end=" ")
print_list(L)
L = quicker_sort(L)
print("After:", end=" ")
print_list(L)

a1 = List()
a2 = List()
a3 = List()

# testing merge functions
n3.next = None
a1.head = n3
a1.tail = n3

n6.next = None
a2.head = n6
a2.tail = n6

n4.next = None
a3.head = n4
a3.tail = n4
# print_list(merge_list([a1, a2, a3]))

