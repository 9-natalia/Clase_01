
#Calculadora

def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def power(a, b):
    if b == 0:
        return 1
    if b >= 1:
        return a * power(a, b - 1)

print("CALCULADORA\n".center(30))

while True:
    try:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        break
    except ValueError:
        continue

opcion = 0

while True:
    print("""
        Dime, ¿qué quieres hacer?

        1) Sumar 
        2) Restar 
        3) Multiplicar 
        4) Dividir 
        5) Potencia
        6) Cambiar los números elegidos
        7) Apagar calculadora
        """)

    while True:
        try:
            opcion = int(input("Elige una opción: "))
            break
        except ValueError:
            continue

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de", n1, "+", n2, "es igual a", suma(n1, n2))
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de", n1, "-", n2, "es igual a", resta(n1, n2))
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de", n1, "*", n2, "es igual a", multiplicar(n1, n2))
    elif opcion == 4:
        print(" ")
        print("RESULTADO: La división de", n1, "/", n2, "es igual a", dividir(n1, n2))
    elif opcion == 5:
        print(" ")
        print("RESULTADO: La potencia de", n1, "^", n2, "es igual a", power(n1, n2))
    elif opcion == 6:
        n1 = float(input("Introduce tu primer número: "))
        n2 = float(input("Introduce tu segundo número: "))
    elif opcion == 7:
        break
    else:
        print("Opción incorrecta")
