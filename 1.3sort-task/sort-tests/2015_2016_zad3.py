# Dana jest struktura Node opisująca listę jednokierunkową: struct Node { Node * next; int value; };
# zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na wejściu listę
# jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że powstała
# z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową wartość.
# Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić wskaźnik
# do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co najmniej
# dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy wejściowej.
# Zakładam ze lista jest posortowana rosnaco


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add(head, node):
    if head is None:
        head = node
    else:
        tmp = head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = node

    return head


def print_list(head):
    curr = head

    while curr:
        print(curr.val, end =" ")
        curr = curr.next
    print("\n")


def cut_node(head):
    # when we cut first element
    if head.val > head.next.val:
        node = head
        head = head.next
    else:
        prev = head
        curr = head.next

        while curr is not None and prev.val < curr.val:
            prev = curr
            curr = curr.next

        node = curr
        prev.next = curr.next
        node.next = None

    # we must return head because head is variable
    return head, node


def insert_node(head, node):
    prev = None
    curr = head
    while curr is not None and node.val > curr.val:
        prev = curr
        curr = curr.next
    if prev is None:
        node.next = head
        head = node
    else:
        node.next = curr
        prev.next = node

    return head


def fix_sorted_list(head):

    head, node = cut_node(head)

    head = insert_node(head, node)

    return head


head = None

n1 = Node(2)
n2 = Node(4)
n3 = Node(1)
n4 = Node(8)
n5 = Node(10)
n6 = Node(12)

head = add(head, n1)
head = add(head, n2)
head = add(head, n3)
head = add(head, n4)
head = add(head, n5)
head = add(head, n6)

print_list(head)
head = fix_sorted_list(head)
print_list(head)
