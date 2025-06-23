def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Ingrese el valor de n: "))
    resultado = fibonacci(n)
    print(f"El término {n} de la secuencia de Fibonacci es: {resultado}")

main()