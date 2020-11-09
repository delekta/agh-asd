def find(left, right, val, tab):
    while right >= left:
        mid = left + (val - tab[left])*(right - left)\
          //(tab[right] - tab[left])
        if tab[mid] == val:
            return mid
        if val > tab[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

tab = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

print(find(0, len(tab) - 1, 7, tab))

