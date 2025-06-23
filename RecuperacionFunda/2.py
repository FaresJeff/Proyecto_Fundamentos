def ordenar_descendente(v):
    for i in range(4):
        for j in range(i + 1, 5):
            if v[i] < v[j]:
                v[i], v[j] = v[j], v[i]
def main():
    vector = [12, 5, 20, 7, 15]
    print("Vector original:", vector)
    ordenar_descendente(vector)
    print("Vector ordenado de mayor a menor:", vector)

main()
