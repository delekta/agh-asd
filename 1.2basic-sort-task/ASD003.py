#Consider a big party where a log register for guest's entry and exits times is maintained. Find the time
#at which there are maximum guests in the party. Note that entries in register are not in any order.
#Input: arr1 = [1, 2, 9, 5, 5]
#       exit = [4, 5, 12, 9, 12]
#Output: 5, There are maximum 3 guests at time 5.
#First people entry then they go out

def maxguests(arr1, exit):
    idxA = 0
    idxE = 0
    people = 0
    max = 0
    arr1 = sorted(arr1)
    exit = sorted(exit)
    while idxA < len(arr1):
        if arr1[idxA] <= exit[idxE]:
            people += 1
            idxA += 1
        else:
            people -= 1
            idxE += 1
        if  people > max:
            max = people
            time = arr1[idxA - 1]

    print(max, ", There are maximum,", max, "guests at time", time)


arr1 = [1, 2, 9, 8, 2, 3]
exit = [7, 5, 12, 9, 12, 12]

maxguests(arr1, exit)