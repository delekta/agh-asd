# Prosze zaimplementowac rekurencyjny algorytm sortujacy liste poprzez jej podzial na 3 listy
# elementow, mniejszych, rownych i wiekszych od pewnego elementu, nastepnie scalajacy
# trzy posortowane listy (quicker sort)


def three_way_partition(arr, left, right):
    start = left
    mid = left
    end = right
    # arr left, remember that you would consider different pieces
    pivot = arr[left]
    while mid <= end:
        if arr[mid] < pivot:
            arr[start], arr[mid] = arr[mid], arr[start]
            start += 1
            mid += 1
        elif arr[mid] > pivot:
            arr[mid], arr[end] = arr[end], arr[mid]
            # mid += 1 because when you swap with end you dont know what is there so you must check it
            end -= 1
        else:
            mid += 1

    return start, end


def quicker_sort(arr, left, right):
    # Warning in recursive functions you cant use while loop!
    if right > left:
        start,  end = three_way_partition(arr, left, right)

        quicker_sort(arr, left, start - 1)
        # The elements are already in place
        # quicker_sort(arr, start, end)
        quicker_sort(arr, end + 1, right)


arr = [5, 6, 7, 2, 5, 5, 5, 2, 9, 42, 7, 5, 5, 13, 3, 4, 6, 7, 3, 6, 9, 9, 7, 2, 3, 1]
# checking three_way_partition
# start, end = three_way_partition(arr, 0, len(arr) - 1)
# print(arr, start, end)

print(arr)
quicker_sort(arr, 0, len(arr) - 1)
print(arr)
