# matrix chain multiplication


# DO DOPRACOWANIA 28.03.2020
def print_brackets(K, BRACKETS, i, j):
    BRACKETS[K[i][j]] += 1
    print_brackets(K, BRACKETS,)

def MCM(rows, columns):
    # Initialization, list filled with inf because we search for min
    C = [[float('inf') for _ in range(len(columns))]for _ in range(len(rows))]
    K = [[float('inf') for _ in range(len(columns))]for _ in range(len(rows))]

    for i in range(len(rows)):
        C[i][i] = 0

    for L in range(2, len(rows) + 1):

        for i in range(len(rows) - L + 1):

            for j in range(i + 1, i + L):

                for k in range(i, j):

                    temp = C[i][j]
                    C[i][j] = min(C[i][j], C[i][k] + C[k + 1][j] + rows[i] * columns[k] * columns[j])

                    if C[i][j] != temp:
                        K[i][j] = k

    BRACKETS = [0] * len(rows)
    print_brackets(K, BRACKETS)
    return C[0][len(rows) - 1]


rows = [3, 2, 4, 2]
columns = [2, 4, 2, 5]
print("Multiplications: ", MCM(rows, columns))

