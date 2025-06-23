def main():
    matriz = [
        [2, 7, 8, 12],
        [3, 5, 32, 6],
        [3, 7, 9, 6],
        [105, 7, 2, 1]
    ]
    ordenar_diagonal_secundaria(matriz)
    for fila in matriz:
        print(fila)
def ordenar_diagonal_secundaria(matrix):
    d = [matrix[i][3 - i] for i in range(4)]
    for i in range(3):
        for j in range(i + 1, 4):
            if d[i] < d[j]:
                d[i], d[j] = d[j], d[i]
    for i in range(4):
        matrix[i][3 - i] = d[i]
main()
