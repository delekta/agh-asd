# Problem: mając dany tekst T i wzorzec P odpowiedzieć na pytanie, czy T zawiera P. Przykład: T =
# aadghhhhhjukipooooopl, P = dghhh, odpowiedź: tak, a dla wzorca P = aadgc, odpowiedź: nie.


def searching(text, pattern):
    const = 37
    highest_const = 1

    pattern_hash = 0
    substr_hash = 0

    for i in range(len(pattern) - 1):
        highest_const *= const

    for i in range(len(pattern)):

        pattern_hash = const * pattern_hash + ord(pattern[i])
        substr_hash = const * substr_hash + ord(text[i])

    for idx in range(len(text) - len(pattern) + 1):

        if pattern_hash == substr_hash:

            j = 0
            while j < len(pattern):

                if text[idx + j] != pattern[j]:
                    break
                j += 1

            if j == len(pattern):
                print("Pattern found at index:", idx)

        if idx < len(text) - len(pattern):

            substr_hash = const * (substr_hash - highest_const * ord(text[idx])) + ord(text[len(pattern) + idx])


text = "aaghhhhhjukipooaghooopl"
pattern = "agh"

searching(text, pattern)
