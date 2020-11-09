# binary heap
# insert method
# The easiest, and the most efficient, way to add an item to a list is to
# simply append the item to the end of the list, but we must to write a method
# that will allow us to regain the heap structure property by comparing newly added
# item with its parent
# we start binary heap from idx = 1
# Min Heap
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def bubbleUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            # i = i // 2 musi byc poza petla
            i = i // 2

    # przy dodawaniu musimy tylko zbubbleUp'owac
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.bubbleUp(self.currentSize)

    def minChild(self, i):
        if self.currentSize < 2 * i + 1:
            return 2 * i
        else:
            if self.heapList[2 * i] < self.heapList[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    # mozemy to bubble down zasatpic heapify i bedzie taka sama zlozonosc? 14.03.2020
    # bubbleDown jest trudniejszy
    def bubbleDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            # zmienna sterujca musi byc poza ifem bo nigdy nie skonczymy while
            i = mc

    def delMin(self):
        res = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        # najwazniejsze
        self.bubbleDown(1)
        return res

    # building heap O(nlogn), each call of heapify costs logn and build heap makes n such calls
    def buildHeap(self, alist):
        i = len(alist) // 2
        # mistrzostwo swiata przy current size
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while(i > 0):
            # bubbleDown z cala mechanika, to heapify_min
            self.bubbleDown(i)
            i -= 1


heap = BinHeap()
heap.insert(12)
heap.insert(2)
heap.insert(31)
heap.insert(19)
heap.insert(14)
heap.insert(24)
heap.insert(64)
heap.insert(10)
heap.insert(6)
popped = heap.delMin()
print(heap.heapList, popped)



