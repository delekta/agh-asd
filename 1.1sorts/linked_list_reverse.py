class Node:
    def __init__(self):
        self.val = None
        self.next = None

def printList(L):
    #you have L != None not L.next != None
    while L != None:
        print(L.val, end=" ")
        L = L.next

def reverse(L):
    if L.next == None : return L
    Temp = L.next
    All = reverse(Temp)
    Temp.next = L
    L.next = None
    return All

L1 = Node() ; L2 = Node() ; L3 = Node()
L1.next = L2 ; L2.next = L3
L1.val = "siema" ; L2.val = "eniu" ; L3.val = "heniu"

printList(L1)
L1 = reverse(L1)
print()
printList(L1)


