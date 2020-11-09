#Omowienie i implementacja jednoczesnego obliczania minimum i maksimum w tablicy n elementowej przy pomocy 3/2n porownan elementow

def minmax(tab):
    l = len(tab)
    idx = 0
    if(l % 2 == 1):
        MIN = MAX = tab[idx]
        idx += 1
    else:
        MIN, MAX = tab[idx], tab[idx + 1]
        idx +=2
    while idx + 1 < l:
        # n/2 porownan
        if tab[idx] < tab[idx + 1]:
            # n/2 porownan
            MIN = min(MIN, tab[idx])
            # n/2 porownan
            MAX = max(MAX, tab[idx + 1])
        else:
            MIN = min(MIN, tab[idx + 1])
            MAX = max(MAX, tab[idx])

        idx += 2

    return MIN, MAX



tab = [2, 3, -5, 7, 11, 3, 1, 120, 15, 27, -4]

min, max = minmax(tab)

print(tab, "min =", min, "max =", max)
