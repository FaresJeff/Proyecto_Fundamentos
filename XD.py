def main():
    numero = pedir_numero()
    resul = fibo_pasos(numero)
    most_res(resul)
def pedir_numero():
    num = input("Ingresa un número: ")
    if val_num(num):
        return int(num)
    else:
        print("Dato no válido, debe ser un número entero no negativo.")
        return pedir_numero()
def val_num(cadena):
    tiene_caracter = False
    for c in cadena:
        if c < "0" or c > "9":
            return False
        tiene_caracter = True
    return tiene_caracter
def most_res(resul):
    print(f"El resultado de Fibonacci es: {resul}")
def fibo_pasos(n):
    a = 1
    b = 1
    print("Pasos del cálculo:")
    paso = 1
    while paso <= n:
        print(f"Paso {paso}: {a}")
        aux = a
        a = b
        b = aux + b
        paso += 1
    return a
main()