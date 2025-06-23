def main():
    notas = []
    for i in range(10):
        notas.append(obtener_nota(i))
        print(f"Alumno {i+1}: {notas[i]}")
def obtener_nota(notas):
    nota = -1
    while nota < 0 or nota > 20:
        nota = float(input(f"Nota {notas+1} (0–20): "))
    return nota
main()