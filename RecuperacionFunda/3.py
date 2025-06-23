def main()->None:
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    area = calcAreaTri(base,altura)
    print("El area del triangulo es: ",area)
def calcAreaTri(base:int,altura:int)->float:
    a: float
    a = (base * altura)/2
    return a
main()

#Ejercicio 3