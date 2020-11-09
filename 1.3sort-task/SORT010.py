# Group anagrams together from given list of words
# Input: arr = [ CARS, REPAID, DUES, NOSE, SIGNED, LANE, PAIRED, ARCS, GRAB, USED, ONES, BRSG, SUED, LEAN, SCAR, DESIGN]
# Output: GRAB BRAG, CARS ARCS SCAR, REPAID PAIRED, LANE LEAN, SIGNED DESIGN, DUES USED SUED, NOSE ONES


# we can use func sort, but i decided to make one
def special_sort(word):
    n = len(word)
    result = []
    while True:
        min_idx = 0
        for j in range(len(word)):
            if word[min_idx] > word[j]:
                min_idx = j
        result.append(word[min_idx])
        word = word[:min_idx] + word[min_idx + 1:]
        if len(result) == n:
            break
    return result


def making_dict(arr):
    dict = {}
    for ele in arr:
        if str(special_sort(ele)) in dict:
            dict[str(special_sort(ele))].append(ele)
        else:
            dict[str(special_sort(ele))] = [ele]
    print(dict)

arr = [ "CARS", "REPAID", "DUES", "NOSE", "SIGNED", "LANE", "PAIRED", "ARCS",
        "GRAB","USED", "ONES", "BRSG", "SUED", "LEAN", "SCAR", "DESIGN"]
making_dict(arr)




