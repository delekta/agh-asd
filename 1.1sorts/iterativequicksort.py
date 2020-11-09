# iterative quicksort


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def iterative_qs(arr, low, high):
    
    stack = [(low, high)]
    
    while len(stack):
        # powinno dzialac bo jak mamy funkcje to tez tak naprawde returnujemy krotke
        low, high = stack.pop()
        # low = low_high[0]
        # high = low_high[1]
        pi = partition(arr, low, high)
        if pi - 1 > low:
            stack.append((low, pi - 1))
        if pi + 1 < high:
            stack.append((pi + 1, high))
            
arr = [2, 3, 32, 23, 12, 53, 11, 5, 9, 3]
iterative_qs(arr, 0, len(arr) - 1)
print(arr)