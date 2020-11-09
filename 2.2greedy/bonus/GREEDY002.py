# Mamy dany ciąg napisów (słów) S = [s1, ..., sn] oraz pewien napis t. Wiadomo, że t można zapisać
# jako złączenie pewnej ilości napisów z S (z powtórzeniami). Na przykład dla S = [s1, s2, s3, s4, s5]
# gdzie s1 = ab, s2 = abab, s3 = ba oraz s4 = bab, s5 = b, napis t = ababbab można zapisać, między innymi,
# jako s2s4 lub jako s1s1s3s5. Taki wybór konkretnych si nazywamy reprezentacją. Przez szerokość reprezentacji
# rozumiemy długość najkrótszego si należącego do reprezentacji - dla s2s4 szerokość to 3, a dla s1s1s3s5
# szerokość to 2. Zaimplementuj algorytm, który mając na wejściu S oraz t znajdzie maksymalną szerokość
# reprezentacji t (tzn. najkrótszy napis w jej reprezentacji jest najdłuższy). Oszacuj czas działania algorytmu.


# complexity O( n * m * k)
# n -> len of words (list of word)
# m -> len of wanted (string)
# k -> average len of word in words
def max_width(words, wanted):

    n = len(wanted)
    # arr for dynamic programming
    dyn_arr = [float('-inf') for _ in range(n)]

    # dynamic programing, fill the array bottom-up
    for idx in range(n):
        for word in words:
            substr = wanted[max(0, idx - len(word) + 1): idx + 1]
            if word == substr:  # check if we can use our word
                if idx - len(word) >= 0:
                    # we take min width from our added word and earlier sequence
                    # cause width is len of shortest word in sequence
                    curr_res = min(len(word), dyn_arr[idx - len(word)])
                else:
                    # because current we have only that one word
                    curr_res = len(word)
                    
                dyn_arr[idx] = max(dyn_arr[idx], curr_res)

    return dyn_arr[-1]


s1 = "ab"
s2 = "abab"
s3 = "ba"
s4 = "bab"
s5 = "b"

t = "ababbab"
S = [s1, s2, s3, s4, s5]

# res  -> abab, bab width = 3
print(max_width(S, t))
