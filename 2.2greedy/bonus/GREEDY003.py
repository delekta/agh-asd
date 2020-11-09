# Cersei i Jaime mają 3 - letniego syna. Przygotowali listę N aktywności podanych jako pary,
# reprezentujące czas rozpoczęcia i zakończenia danej aktywności. Zaimplementuj algorytm,
# który przyporządkuje każdej aktywności literę C lub J, oznaczającą, że daną aktywność
# z synem wykona odpowiednio Cersei lub Jaime, w taki sposób, że żaden rodzic nie wykonuje pokrywających
# się czasowo aktywności. Jeżeli takie przyporządkowanie nie istnieje, to algorytm zwraca “IMPOSSIBLE”,
# a jeśli istnieje, to zwraca odpowiedniego stringa.
# Przykładowo: (99, 150), (1, 100), (100, 301), (2,5), (150, 250) - odpowiedź to JCCJJ (lub CJJCC).
# Posortować przedziały po poczatkach


def partition(arr, left, right):
    pivot = arr[right][0]
    i = left - 1
    for j in range(left, right):
        if arr[j][0] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def sort_by_start(arr, left, right):
    if right > left:
        q = partition(arr, left, right)
        sort_by_start(arr, left, q - 1)
        sort_by_start(arr, q + 1, right)


def activities(actv):
    lastC = 0
    lastJ = 0
    sort_by_start(actv, 0, len(actv) - 1)
    print(actv)
    res = ""
    for act in actv:
        if lastC <= act[0]:
            res = res + "C"
            lastC = act[1]
        elif lastJ <= act[0]:
            res = res + "J"
            lastJ = act[1]
        else:
            return False, res

    return True, res


actv = [(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)]

print(activities(actv))
