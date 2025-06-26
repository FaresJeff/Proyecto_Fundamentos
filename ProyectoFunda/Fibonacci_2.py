def Fibonacci(numero):
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    else:
        return Fibonacci(numero - 1) + Fibonacci(numero - 2)

for i in range (10):
    print(Fibonacci)