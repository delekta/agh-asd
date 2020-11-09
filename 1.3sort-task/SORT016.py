"""
W szeregu ustawiło się 2n żołnierzy. Połowa z nich to zwykli szeregowi, a połowa to siły specjalne.
Mieli się ustawić na 2 grupy: najpierw szeregowi, a potem specjalni, ale sierżant zapomniał im o tym powiedzieć.
Stoją teraz przypadkowo, z odstępem 1 metra pomiędzy kolejnymi żołnierzami. Szereg to lista struktur typu:
class Soldier:
    type = False  # is a special soldier?
    next = None
Zaimplementuj funkcję distanceToIdeal(firstSoldier), która oblicza najmniejszą liczbę metrów,
 jaką żołnierze muszą sumarycznie przejść, żeby szeregowi stali po lewej od żołnierzy specjalnych
 (i żeby cały szereg dalej stał w tym samym miejscu).
Uwaga: nie wymaga się sortowania listy.

"""
class Soldier:
    def __init__(self, special=False): # is a special soldier
        self.type = special
        self.next = None


def print_list(first):
    p = first
    while p:
        if p.type is True:
            print(1, end =" ")
        else:
            print(0, end=" ")
        p = p.next


def make_list(first):
    end = None
    while True:
        print("Enter -1 if you want to end")
        special = int(input("Enter 1 if it is special soldier, if not 0"))
        if special == -1:
            break
        if special == 1:
            new_s = Soldier(True)
        else:
            new_s = Soldier(False)

        if first is None:
            first = new_s
            end = first
        else:
            end.next = new_s
            end = end.next

        print_list(first)
    # musisz returnowac bo obiekty nie sa przez referencje
    return first

def how_many_meters(first):
    h = first
    soldier_num = 0
    step_num = 0
    while h:
        if h.type is False:
            soldier_num += 1
        else:
            step_num += soldier_num * 2
        h = h.next

    return step_num


first = None
first = make_list(first)
print_list(first)
print(how_many_meters(first))