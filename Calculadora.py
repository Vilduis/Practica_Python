#Calculadora simple

def suma(numero1,numero2):
    return numero1 + numero2

def resta(numero1,numero2):
    return numero1 - numero2

def multiplicacion(numero1,numero2):
    return numero1 * numero2

def division(numero1,numero2):
    return numero1 / numero2 if numero2 != 0 else "Error: No se puede dividir entre 0"


def menu():
    print("\n----Menu de opciones----")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")

    opcion=int(input("Ingrese una opcion:"))

    if opcion == 1:
        numero1=int(input("Ingrese el primer numero:"))
        numero2=int(input("Ingrese el segundo numero:"))
        print("La suma es:",suma(numero1,numero2))
    elif opcion == 2:
        numero1=int(input("Ingrese el primer numero:"))
        numero2=int(input("Ingrese el segundo numero:"))
        print("La resta es:",resta(numero1,numero2))
    elif opcion == 3:
        numero1=int(input("Ingrese el primer numero:"))
        numero2=int(input("Ingrese el segundo numero:"))
        print("La multiplicacion es:",multiplicacion(numero1,numero2))
    elif opcion == 4:
        numero1=int(input("Ingrese el primer numero:"))
        numero2=int(input("Ingrese el segundo numero:"))

        if numero2 == 0:
            numero2 = int(input("Error: No se puede dividir entre 0. Ingrese un segundo numero diferente de 0:"))

        print("La division es:",division(numero1,numero2))
    else:
        print("\nOpcion no valida. Intente de nuevo.")
        menu()


while True:
    menu()
    Seguir = input("\n¿Deseas continuar? (s/n):").lower()
    if Seguir != "s":
        break