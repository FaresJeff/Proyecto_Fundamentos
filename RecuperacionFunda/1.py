def main():
    notas = []
    for i in range(10):
        notas.append(validar_nota(i))
    print("Notas registradas:", notas)
def validar_nota(i):
    nota = -1
    while nota < 0 or nota > 20:
        nota = float(input(f"Nota {i+1} (0–20): "))
    return nota
main()