# (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n×n. Szachownica zawiera liczby wymierne.
# Należy przejść z pola (1,1) na pole (n,n) korzystając jedynie z ruchów “w dół” oraz “w prawo”. Wejście na
# dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm znajdujący trasę o minimalnym koszcie.
# funkcja: f[i][j] = min(f[i - 1][j], f[i][j - 1]) + value[i][j], f(i, j) -> minimalny koszt dojscia do pola f(i, j)

def min_path(arr):
    result = [[0 for _ in range(len(arr))] for _ in range(len(arr))]

    sum_row = 0
    sum_column = 0
    for i in range(len(result)):
        sum_column += arr[i][0]
        sum_row += arr[0][i]

        result[i][0] = sum_column
        result[0][i] = sum_row

    for i in range(1, len(result)):
        for j in range(1, len(result)):
            result[i][j] = min(result[i - 1][j], result[i][j - 1]) + arr[i][j]

    print(result)
    return result[len(result) - 1][len(result) - 1]


arr = [
    [1, 3, 5, 9, 4],
    [4, 4, 3, 9, 4],
    [6, 3, 3, 9, 4],
    [2, 3, 2, 1, 5],
    [1, 3, 5, 1, 4],
]

print(min_path(arr))
