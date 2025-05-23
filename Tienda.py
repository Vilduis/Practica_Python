hombre_ropa = [
    {
        "tipo": "pantalones",
        "marca": "fndkf",
        "precio": 101.94
    },
    
]

mujer_ropa = [
    {
        "tipo": "pantalones",
        "marca": "fndkf",
        "precio": 101.94
    },
    
]

def hombre():
    print("1.Pantalones")
    print("2.Camisas")
    print("3.Casacas")
    print("4.Polos")

    opcion=input("¿Que sea ver?:").lower()

    if opcion == "pantalones":
        print("----Lista de pantalones----")

        for prenda in hombre_ropa:
            if prenda["tipo"] == opcion:
             print(f"{prenda['tipo'].capitalize()} - Marca: {prenda['marca']}, Precio: s/ {prenda['precio']}")
        
        print("----Elije un marca----")

        opcion_marca=input("Ingrese la marca que desea comprar:")
        cantidad = int(input("Ingrese la cantidad que desea comprar:"))

        for prenda in hombre_ropa:
            if prenda["tipo"] == opcion and prenda["marca"] == opcion_marca:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']* cantidad}")

    elif opcion == "camisas":
        print("----Lista de camisas----")
        for prenda in hombre_ropa:
            if prenda["tipo"] == opcion:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']}")
        
        print("----Elije un marca----")

        opcion_marca=input("Ingrese la marca que desea comprar:")
        cantidad = int(input("Ingrese la cantidad que desea comprar:"))

        for prenda in hombre_ropa:
            if prenda["tipo"] == opcion and prenda["marca"] == opcion_marca:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']* cantidad}")

    elif opcion == "casacas":
        print("----Lista de casacas----")
        for prenda in hombre_ropa:
            if prenda["tipo"] == opcion:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']}")

        print("----Elije un marca----")

        opcion_marca=input("Ingrese la marca que desea comprar:")
        cantidad = int(input("Ingrese la cantidad que desea comprar:"))

        for prenda in hombre_ropa:
            if prenda["tipo"] == opcion and prenda["marca"] == opcion_marca:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']* cantidad}")

    elif opcion == "polos":
        print("----Lista de polos----")
        for prenda in hombre_ropa:
            if prenda["tipo"] == opcion:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']}")
        
        print("----Elije un marca----")

        opcion_marca=input("Ingrese la marca que desea comprar:")
        cantidad = int(input("Ingrese la cantidad que desea comprar:"))

        for prenda in hombre_ropa:
            if prenda["tipo"] == opcion and prenda["marca"] == opcion_marca:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']* cantidad}")
    else:
        print("No tenemos esa ropa disponible")
        print("----Fin de la busqueda----")

def mujer():
    print("1.Pantalones")
    print("2.Abrigos, Blazers y chalecos")
    print("3.Blusas")
    print("4.Chompas")

    opcion=input("¿Que sea ver?:").lower()

    if opcion == "pantalones":
        print("----Lista de pantalones----")

        for prenda in mujer_ropa:
            if prenda["tipo"] == opcion:
             print(f"{prenda['tipo'].capitalize()} - Marca: {prenda['marca']}, Precio: s/ {prenda['precio']}")
        
        print("----Elije un marca----")

        opcion_marca=input("Ingrese la marca que desea comprar:")
        cantidad = int(input("Ingrese la cantidad que desea comprar:"))

        for prenda in  mujer_ropa:
            if prenda["tipo"] == opcion and prenda["marca"] == opcion_marca:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']* cantidad}")

    elif opcion == "abrigos" or opcion == "blazers" or opcion == "chalecos":
        print("----Lista de abrigos-blazers-chalecos----")
        for prenda in  mujer_ropa:
            if prenda["tipo"] == opcion:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']}")
        
        print("----Elije un marca----")

        opcion_marca=input("Ingrese la marca que desea comprar:")
        cantidad = int(input("Ingrese la cantidad que desea comprar:"))

        for prenda in  mujer_ropa:
            if prenda["tipo"] == opcion and prenda["marca"] == opcion_marca:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']* cantidad}")

    elif opcion == "blusas":
        print("----Lista de blusas----")
        for prenda in  mujer_ropa:
            if prenda["tipo"] == opcion:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']}")

        print("----Elije un marca----")

        opcion_marca=input("Ingrese la marca que desea comprar:")
        cantidad = int(input("Ingrese la cantidad que desea comprar:"))

        for prenda in  mujer_ropa:
            if prenda["tipo"] == opcion and prenda["marca"] == opcion_marca:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']* cantidad}")

    elif opcion == "chompas":
        print("----Lista de chompas----")
        for prenda in  mujer_ropa:
            if prenda["tipo"] == opcion:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']}")
        
        print("----Elije un marca----")

        opcion_marca=input("Ingrese la marca que desea comprar:")
        cantidad = int(input("Ingrese la cantidad que desea comprar:"))

        for prenda in  mujer_ropa:
            if prenda["tipo"] == opcion and prenda["marca"] == opcion_marca:
             print(f"{prenda['tipo'].capitalize()} - Marca {prenda['marca']}, Precio: s/ {prenda['precio']* cantidad}")
    else:
        print("No tenemos esa ropa disponible")
        print("----Fin de la busqueda----")


def eres_hombre_mujer():
    print("1.Hombre")
    print("2.Mujer")
    personalidad=int(input("Ingrese su genero:"))

    if personalidad == 1:
        hombre()
    else:
        mujer()

def menu():
    print("----Bienvenido a mi tienda de ropa----")
    eres_hombre_mujer()


menu()