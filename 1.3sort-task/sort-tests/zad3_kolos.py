# Zadanie 3
# Mamy dane k posortowanych niemalejaco list. Kazda lista zawiera dokladnie n liczb calkowitych.
# Prosze zaproponowac algorytm, ktory zwraca przedzial zamkniety[a, b] o nastepujacych wlasnosciach:
# 1. kazda lista zawiera co najmniej jedna liczbe z przedzialu [a, b].
# 2. wartosci b - a(czyli dlugosc przedzialu) jest minimalna.
# Algorytm powininen byc mozliwie najszybszy. Nalezy uzasadnic poprawnosc i oszacowac zlozonosc czasowa.
# W tym zadaniu nie wymaga implementaacji.
# Przyklad. Dla trzech list L1 = [4, 7, 9, 12, 15], L2 = [0, 8, 10, 14, 20], L3 = [6, 12, 16, 30, 50]
# przykladowy przedzial spelniajacy warunki zadania to [6, 8].


class Element:
    def __init__(self, val, list, idx):
        self.val = val
        self.list = list
        self.idx = idx


class Heap:
    def __init__(self):
        self.size = 0
        self.arr = []
        self.popped = False

    def append(self, val, list, idx):
        el = Element(val, list, idx)
        self.arr.append(el)
        self.size += 1

    # Time complexity: log(n)
    def heapify_min(self, root):
        left = 2 * root + 1
        right = 2 * root + 2

        mini = root
        if left < self.size and self.arr[left].val < self.arr[mini].val:
            mini = left
        if right < self.size and self.arr[right].val < self.arr[mini].val:
            mini = right
        if mini != root:
            self.arr[mini], self.arr[root] = self.arr[root], self.arr[mini]
            self.heapify_min(mini)

    # Time complexity of building heap i O(n)
    def build_heap(self):
        for i in range((self.size // 2) - 1, -1, -1):
            self.heapify_min(i)

    def get_min(self):
        return self.arr[0]

    def replace_min(self, val, list, idx):
        el = Element(val, list, idx)
        self.arr[0] = el
        self.heapify_min(0)


def find_smallest_range(arr, k, n):
    heap = Heap()

    max_val = float('-inf')
    min_range = float('inf')
    a = -1
    b = -1

    for i in range(k):
        heap.append(arr[i][0], i, 0)
        if arr[i][0] > max_val:
            max_val = arr[i][0]
    heap.build_heap()

    while True:

        min_el = heap.get_min()

        min_val = min_el.val

        if max_val - min_val < min_range:
            a = min_val
            b = max_val
            min_range = max_val - min_val

        if min_el.idx + 1 < n:
            heap.replace_min(arr[min_el.list][min_el.idx + 1], min_el.list, min_el.idx + 1)
            # Updating max -> really important line!!!
            if arr[min_el.list][min_el.idx + 1] > max_val:
                max_val = arr[min_el.list][min_el.idx + 1]
        else:
            break

    print("Min range: [", a, ", ", b, "]")


arr = [
    [4, 7, 9, 12, 15],  # L1
    [0, 8, 10, 14, 20],  # L2
    [6, 12, 16, 30, 50],  # L3
]

k =3
n = len(arr)
find_smallest_range(arr, 3, n)

