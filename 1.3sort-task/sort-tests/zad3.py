# Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimumc(array-based heap).
# Mając daną liczbę rzeczywistą x sprawdź, czy k-ty najmniejszy element jest większy lub równy x. 

# Nieoptymalnie: sprawdzać elementy po kolei metodą pop() - O(k*log(n)).

# Optymalnie:
# Zauważmy, że z definicji kopca minimum każdy korzeń poddrzewa jest mniejszy od wszystkich swoich dzieci.
# Dotyczy to zarówno korzenia całego kopca, jak i wszystkich poddrzew. Wynika z tego, że jeżeli korzeń jest >= x,
# to całe poddrzewo musi być >= x (skoro nic nie może być tam mniejszego, to może być tylko większe lub równe).
# Zauważmy także, że nie interesuje nas wartość wierzchołków przed k-tym. Co więcej, nie interesuje nas nawet
# wartość k-tego wierzchołka - interesuje nas tylko jego relacja z x, czy jest od niego mniejszy, czy większy lub równy.
# Można przejść po drzewie kopca (przydatne są tutaj funkcje pomocnicze get_left_child(i), get_right_child(i)
# oraz get_parent(i)) przeszukując dzieci wszystkich wierzchołków o wartości mniejszej od x, aż:
# znajdziemy przynajmniej k wierzchołków o wartości < x; jeżeli tak się stanie, to k-ty wierzchołek musiał być
# mniejszy od x, a więc zwracamy fałsz
# wyczerpiemy wierzchołki o wartości < x, zanim znaleźliśmy ich k; jeżeli tak się stanie, to dalsze wierzchołki
# muszą być >= x, a zatem k-ty też, więc zwracamy prawdę
# Złożoność: sprawdzamy tylko dzieci wierzchołków o wartości < x, a tych jest co najwyżej k (jeżeli byłoby więcej,
# to przerywamy zgodnie z opisem powyżej); każde może mieć co najwyżej 2 dzieci, więc odwiedzamy co najwyżej
# 3k wierzchołków, a więc mamy O(k).


def parent(idx):
    return (idx - 1) // 2


def left_child(idx):
    return idx * 2 + 1


def right_child(idx):
    return idx * 2 + 2


# return how many is < x, because if k elements are < x this mean k'th is < x
# if we check < x we cut tree and time complexity is better than >= x
def check(arr, x, idx=0, c=0):
    if arr[idx] < x:
        c += 1
    else:
        # because we dont want to search in that subtree
        return c

    if left_child(idx) < len(arr):
        c = check(arr, x, left_child(idx), c)

    if right_child(idx) < len(arr):
        c = check(arr, x, right_child(idx), c)

    return c


arr = [2, 4, 6, 11, 5, 7, 8, 15, 13]

x = 10
print(check(arr, x))

