# Proszę zaimplementować funkcję sortującą (rosnąco) listę jednokierunkową metodą QuickerSort. Algorytm QuickerSort
# to odmiana algorytmu QuickSort, w której funkcja podziału dzieli sortowane dane według przyjętej wartości x n
# a trzy grupy: mniejsze od x, równe x, oraz większe od x. Następnie rekurencyjnie sortowane są grupy pierwsza
# i trzecia. Państwa funkcja powinna mieć następujący prototyp:
# struct Node { Node* next; int val; }; Node* QuickerSort ( Node* head )
# Argumentem funkcji jest wskaźnik na głowę listy do posortowania a wynikiem powinien być wskaźnik na głowę
# listy posortowanej. Sortowanie powinno polegać na porównywaniu wartości val list oraz przepinaniu wskaźników next.


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def merge_list(list_of_list):
    result_head = None
    result_tail = None
    for head, tail in list_of_list:
        if head is not None:
            if result_head is None:
                result_head = head
                result_tail = tail
            else:
                # must be result_tail.next not result.tail
                result_tail.next = head
                result_tail = tail

    return result_head, result_tail


def is_empty(head):
    return head is None


def has_one_enemy(head, tail):
    return head is tail


def add(node, head, tail):
    node.next = None
    if head is None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node

    # must be returned because they are variables
    return head, tail


def quicker_sort(head, tail):
    if is_empty(head) or has_one_enemy(head, tail):
        return head, tail

    curr = head

    smaller_head = None
    smaller_tail = None

    equal_head = None
    equal_tail = None

    greater_head = None
    greater_tail = None

    pivot = tail.val

    while curr:
        # important
        temp = curr.next
        if curr.val < pivot:
            smaller_head, smaller_tail = add(curr, smaller_head, smaller_tail)
        elif curr.val == pivot:
            equal_head, equal_tail = add(curr, equal_head, equal_tail)
        else:
            greater_head, greater_tail = add(curr, greater_head, greater_tail)
        curr = temp

    return merge_list([quicker_sort(smaller_head, smaller_tail), (equal_head, equal_tail), quicker_sort(greater_head, greater_tail)])


def print_list(head):
    curr = head

    while curr:
        print(curr.val, end =" ")
        curr = curr.next
    print("\n")

head = None
tail = None

n1 = Node(4)
n2 = Node(2)
n3 = Node(9)
n4 = Node(7)
n5 = Node(6)
n6 = Node(8)

head, tail = add(n1, head, tail)
head, tail = add(n2, head, tail)
head, tail = add(n3, head, tail)
head, tail = add(n4, head, tail)
head, tail = add(n5, head, tail)
head, tail = add(n6, head, tail)

print_list(head)
head, tail = quicker_sort(head, tail)
print_list(head)

