#  Dane są następujące struktury: struct Node { Node* next; int val; }; struct TwoLists { Node* even; Node* odd; };
#  Napisać funkcję: TwoLists split(Node* list); Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste
#  i drugą zawierającą liczby nieparzyste. Listy nie zawierają wartowników.


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


def two_list_split(head):
    # we create odd list
    head_odd = None
    last_odd = None

    prev = head
    curr = head.next

    node = None
    while curr:
        # when we cut first element
        if head.val % 2 == 1:
            node = head
            head = head.next
            node.next = None

            prev = head
            curr = head.next
        else:
            if curr.val % 2 == 1:
                node = curr
                prev.next = curr.next

                curr = curr.next

                node.next = None
            else:
                prev = curr
                curr = curr.next

        # we have cut node
        if node is not None:
            if head_odd is None:
                head_odd = node
                last_odd = node
            else:
                last_odd.next = node
                last_odd = last_odd.next

        # because changing pointers depends of what happens!!!
        # prev = curr
        # curr = curr.next
        node = None


    # head is head_even
    return head, head_odd


head = None

n1 = Node(2)
n2 = Node(3)
n3 = Node(16)
n4 = Node(7)
n5 = Node(10)
n6 = Node(12)

head = add(head, n1)
head = add(head, n2)
head = add(head, n3)
head = add(head, n4)
head = add(head, n5)
head = add(head, n6)

head_even, head_odd = two_list_split(head)
print_list(head_even)
print_list(head_odd)
