# Sortowanie liniowe
# Zadanie 3
# Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności O(n), który stwierdza,
# czy w tablicy ponad połowa elementów ma jednakową wartość.
# Drugi sposob: Podejscie z Bucket Sort
# Lookups to python dictionary is O(1)
# Checking if key exists
# If you use:
#     if key in dict:
# It’s O(n)
#
# if you use:
#     if dict.get(key):
# It’s O(1)

def half_of_elements(arr):
    n = len(arr)
    dic = {}
    for el in arr:
        if dic.get(el):
            dic[el] += 1
            if dic[el] == (n // 2) + 1:
                print(dic)
                return True
        else:
            dic[el] = 1

    print(dic)
    return False


arr = [1, 2, 2, 2, 4, 2, 4, 2, 7, 1, 2, 3]
print(half_of_elements(arr))