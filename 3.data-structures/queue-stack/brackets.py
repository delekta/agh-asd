# Proszę zaimplementować algorytm, który majęc na wejściu napis zbudowany z
# nawiasow (, ), [, i ] sprawdza czy nawiasowanie jest poprawne.


class StackA:
    def __init__(self, length):
        self.arr = [None] * length
        self.length = length
        self.size = 0

    def push(self, element):
        self.arr[self.size] = element
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.arr[self.size]

    def top(self):
        return self.arr[self.size - 1]

    def is_empty(self):
        return self.size == 0


def brackets(string):
    S = StackA(len(string))
    for char in string:
        if char == '(' or char == '[':
            S.push(char)
        elif char == ')':
            if S.pop() != '(':
                return False
        elif char == ']':
            if S.pop() != '[':
                return False
    if S.is_empty():
        return True
    else:
        return False


string1 = "(q)(aa(as))[aa()]"
string2 = "(q](aa(as))[aa()]"
string3 = "((scdds)"

print("1. ", brackets(string1))
print("2. ", brackets(string2))
print("3. ", brackets(string3))
