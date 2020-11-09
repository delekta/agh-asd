# Given a linked list containing 0's, 1's, 2's, sort linked list by doing single traversal of it
# Simple solution would be to count number 0f 0's, 1's and 2's present in the linked list and traverse
# the linked list and put them back in correct order. The problem with this approach is that we need to
# do two traverslals of the list which violets the problem constraits.

# We can solve this problem in single traersal of the list. The idea is to maintain three pointers
# zeros, ones and twos. Then, we trawerse the list from head to end and move each node to the corresponding
# depending on its value. Finally, we combine all three lists at the end and fix the head pointer

class Node:
    def __init__(self):
        self.val = None
        self.next = None


def printList(head):
    curr = head
    while curr != None:
        print(curr.val, end=" ")
        curr = curr.next


def makeList(head):
    end = -1
    while True:
        print("Wcisnij \"5\" jesli chcesz zakończyć tworzenie listy:")
        end = int(input("Podaj wartosc node:"))
        if end == 5:
            break
        p = Node()
        p.val = end
        p.next = head
        head = p
        printList(head)

    return head



def sort(head):
    curr = head
    first0 = None; first1 = None; first2 = None
    last0 = Node(); last1 = Node(); last2 = Node()

    while curr != None:
        tmp = curr.next
        idx = curr.val

        if idx == 0:
            if first0 == None:
                last0 = curr
            curr.next = first0
            first0 = curr
        elif idx == 1:
            if first1 == None:
                last1 = curr
            curr.next = first1
            first1 = curr
        else:
            if first2 == None:
                last2 = curr
            curr.next = first2
            first2 = curr

        curr = tmp
    last2.next = None
    last1.next = first2
    last0.next = first1

    head = first0
    return head


head = None
head = makeList(head)
head = sort(head)
printList(head)




