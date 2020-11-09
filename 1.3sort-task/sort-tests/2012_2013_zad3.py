# Proszę napisać funkcję bool possible( char* u, char* v, char* w ), która zwraca prawdę jeśli z liter
# słów u i v da się ułożyć słowo w (nie jest konieczne wykorzystanie wszystkich liter) oraz fałsz w przeciwnym wypadku.
# Można założyć, że w i v składają się wyłącznie z małych liter alfabetu łacińskiego.
# Proszę krótko uzasadnić wybór zaimplementowanego algorytmu.
# Time complexity: nlogn, we can do it in O(n) simply count[0..26] count number of chars in u and v
# then we can check if we have enough letter to create w(if we find 0 count return FALSE

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quicksort(arr, left, right):
    if right > left:
        q = partition(arr, left, right)
        quicksort(arr, left, q - 1)
        quicksort(arr, q + 1, right)


def possible(word1, word2, searched):
    word1_arr = [word1[i] for i in range(len(word1))]
    word2_arr = [word2[i] for i in range(len(word2))]
    searched_arr = [searched[i] for i in range(len(searched))]

    # we can also use built_in function word1_arr = sorted(word1)
    quicksort(word1_arr, 0, len(word1_arr) - 1)
    quicksort(word2_arr, 0, len(word2_arr) -1)
    quicksort(searched_arr, 0, len(searched_arr) - 1)

    print(word1_arr, "\n", word2_arr, "\n", searched_arr)

    w1, w2, s = 0, 0, 0
    # once step at a time
    while w1 < len(word1) and w2 < len(word2):
        if word1_arr[w1] < word2_arr[w2]:
            if word1_arr[w1] == searched_arr[s]:
                w1 += 1
                s += 1
            else:
                w1 += 1
        else:
            if word2_arr[w2] == searched_arr[s]:
                w2 += 1
                s += 1
            else:
                w2 += 1
        if s == len(searched_arr):
            return True

    while w1 < len(word1_arr):
        if word1_arr[w1] == searched_arr[s]:
            w1 += 1
            s += 1
        else:
            w1 += 1
        if s == len(searched_arr):
            return True

    while w2 < len(word2_arr):
        if word2_arr[w2] == searched_arr[s]:
            w2 += 1
            s += 1
        else:
            w2 += 1
        if s == len(searched_arr):
            return True

    return False


# testing sorting string by sorted
# word = "ananas"
# print(word)
# word = sorted(word)
# print(word)

word1 = "key"
word2 = "segment"
searched = "geeks"
print(possible(word1, word2, searched))
