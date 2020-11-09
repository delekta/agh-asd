# Proszę zaprojektowac strukturę danych przechowującą liczby i pozwalającą na następujące
# operacje (zakładamy, że wszystkie liczby umieszczane w strukturze są różne):
# Init(n). Tworzy zadaną strukturę danych zdolną pomieścić maksymalnie n liczb.
# Insert(x). Dodaje do struktury liczbę x.
# RemoveMin() Znajduje najmniejszą liczbę w strukturze, usuwa ją i zwraca jej wartość.
# RemoveMax() Znajduje największą liczbę w strukturze, usuwa ją i zwraca jej wartość.
# Każda z operacji powinna mieć złożoność O(logn, gdzie n to ilość liczb znajdujących się obecnie
# w strukturze. W tym zadaniu nie trzeba implementować podanych operacji, a jedynie przekonująco opisać jak powinny
# być zrealizowane i dlaczego mają wymaganą złożoność
#
# Garek Solution:
#   Dwa kopce min i max, kazdy element to krotka (val, idx_in_second_heap) Do zaimplementowania!!!
#   Gdy usuwamy min to w heap_min zamieniamy z z ostanim i heapify(0), w heap[0][idx_in_second_heap] tez zamieniamy z
#   ostatnim i heapify(idx_in_second_heap). Przy obu operacjach size -= 1.
#
# Advanced Solution:
#   Min-max heap - The min-max heap property is: each node at an even level in the tree is less than all
#   of its descendants, while each node at an odd level in the tree is greater than all of its descendants.


