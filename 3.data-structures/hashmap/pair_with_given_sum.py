# Problem: Mając daną na wejściu tablicę liczb naturalnych napisać procedurę odpowiadającą na pytanie, czy
# istnieje para liczb sumujących się do zadanej innej liczby. Przykład: [12, 3, 4, 90, 15, 55], liczba = 19 -> tak: 15
# + 4.


def pair_with_given_sum(arr, searched):
    s = set()
    for el in arr:
        if searched - el in s:
            return True
        else:
            s.add(el)
    return False


arr = [12, 3, 4, 90, 15, 55]
searched = 70

print(pair_with_given_sum(arr, searched))
