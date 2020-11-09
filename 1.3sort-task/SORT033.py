# Zadanie 11
# Zaproponuj algorytm, który w czasie O(nlog(n)) posortuje stos o rozmiarze n. Dozwolone jest tylko
# wykorzystywanie operacji udostępnionych przez interfejs stosu: push(), pop(), top(), isEmpty(), oraz
# dodatkowych stosów.
# Wskazowka: Potrzeba 3 dodatkowych stosów. ściągamy z początkowego stosu tak długo jak są posortowane i idkładamy na drugi stos. Potem tak
# samo na trzeci stos. Te da stosy scalamy na czwarty stos. Powtarzamy takie ściąganie list naturalnych aż pierwszy stos będzie pusty.
# Wtedy czwarty stos staje się pierwszy i operację kontynuujemy, aż ściągniećie listy naturalnej będzie ściągnięciem całego stosu.


# Do poprawy 26.03.2020
# Exceed recursion depth
class Stack:
    def __init__(self):
        self.item = []

    def push(self, el):
        self.item.append(el)

    def pop(self):
        return self.item.pop()

    def top(self):
        return self.item[len(self.item) - 1]

    def empty(self):
        return self.item == []


def merge(s4, s2, s3):
    while not s2.empty and not s3.empty:
        if s2.top() < s3.top():
            s4.push(s2.pop())
        else:
            s4.push(s3.pop())

    while not s2.empty:
        s4.push(s2.pop())
    while not s3.empty:
        s4.push(s3.empty)


def stack_sort(s1, s2, s3, s4):
    if not s1.empty():
        while ((not s1.empty()) and (s2.empty() or s2.top() > s1.top())):
            s2.push(s1.pop())
        while ((not s1.empty()) and (s3.empty or s3.top() > s1.top())):
            s3.push(s1.pop())

        if s1.empty() and s3.empty() and s4.empty():
            return s2
        merge(s4, s2, s3)

    if not s1.empty():
        return stack_sort(s1, s2, s3, s4)
    else:
        return stack_sort(s4, s2, s3, s1)


s1 = Stack()
s1.push(4)
s1.push(2)
s1.push(1)
s1.push(7)
s1.push(9)
s1.push(19)
s1.push(3)

tmp1 = Stack()
tmp2 = Stack()
tmp3 = Stack()

s = stack_sort(s1, tmp1, tmp2, tmp3)

while not s.empty:
    print(s.pop())



