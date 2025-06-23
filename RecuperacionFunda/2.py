def ordenar_descendente(vector):
    for i in range(4):
        for j in range(i + 1, 5):
            if vector[i] < vector[j]:
                vector[i], vector[j] = vector[j], vector[i]
def main():
    vector = [12, 5, 20, 7, 15]
    print("Vector original:", vector)
    ordenar_descendente(vector)
    print("Vector ordenado de mayor a menor:", vector)

main()

#Ejercicio 2