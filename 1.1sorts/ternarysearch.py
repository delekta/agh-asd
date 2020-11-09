def ternarysearch(left, right, val, tab):
    while right >= left:
        mid_left = left + (right - left) // 3
        mid_right = right - (right - left) // 3
        if(tab[mid_left] == val):
            return mid_left
        elif(tab[mid_right] == val):
            return mid_right
        if val < tab[mid_left]:
            right = mid_left - 1
        elif val > tab[mid_right]:
            left = mid_right + 1
        else:
            left = mid_left + 1
            right = mid_right - 1
    return -1

tab = [2, 3, 5, 7, 9, 11, 14, 17, 25, 25, 25, 29, 34, 53]

print(ternarysearch(0, len(tab) - 1, 5, tab))