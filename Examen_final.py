#PREGUNTA 1 - TEMA C
#-*- coding: 1252 *



import os
import math

def cantidad_primos(n):
    cantidad = 0
    for i in range(2, n):
        if n % i == 0:
            cantidad += 1
    return cantidad

def calcular_suma(n, x):
    resultado = 1
    for i in range(1, n + 1):
        resultado += (pow(-1, i) * (pow(2, 2 * i - 1) * pow(x, 2 * i)) / math.factorial(2 * i))
    return resultado

def menu():
    print("===Menu de opciones")
    print("1. Hallar cantidad de digitos no primos")
    print("2. Calcular Serie")
    print("3. Fin")
   
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        numero = -1
        while not numero > 0:
            numero = int(input("Ingrese el valor de N: "))
            if numero > 0:
                print("Cantidad de digitos no primos: ", cantidad_primos(numero))
    elif opcion == 2:
        n = -1
        while not n >= 10 and n <= 25:
            n = int(input("Ingrese el valor de N: "))
        x = int(input("Ingrese el valor de N: "))
        print("El resultado de la suma es ", calcular_suma(n, x))
    elif opcion == 3:
        print("Fin del programa")
        os._exit(0)
    else:
        print("Opcion incorrecta")
        os.system("cls")
    menu()

menu()
#PREGUNTA 2 – TEMA A
#-*- coding: 1252 *
import random

def verificar_primo(numero):
    if numero == 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

elementos = random.randint(1, 50)
numeros = []
no_primos_lista = []
for i in range(elementos):
    numeros.append(random.randint(50, 1000))
no_primos = 0
for numero in numeros:
    if not verificar_primo(numero):
        no_primos += 1
        no_primos_lista.append(numero)
print("Cantidad de números no primos: {}".format(no_primos_lista))
print("Números no primos: {}".format(no_primos))
numero_menos = min(numeros)
print("Número menor: {}".format(numero_menos))
veces_repirte = numeros.count(numero_menos)
print("Veces que se repite el número menor: {}".format(veces_repirte))
numeros_descendente = sorted(numeros, reverse=True)
print("Ordenado descendente: {}".format(numeros_descendente))
#PREGUNTA 3 – TEMA B
import random

class  CEncuesta :
    def _init_(self):
        self.__edad = None
        self.__sexo = None
        self.__Servicio_video_llamadas=None
        self.__Nivel_de_satisfacción = None
       

    def _init_(self, edad, sexo, Servicio_video_llamadas, Nivel_de_satisfacción):
        self.__edad = edad
        self.__sexo = sexo
        self.__Servicio_video_llamadas = Servicio_video_llamadas
        self.__Nivel_de_satisfacción = Nivel_de_satisfacción

    def set_edad(self, edad):
        self.__edad = edad

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_Servicio_video_llamadas(self, Servicio_video_llamadas):
        self.__Servicio_video_llamadas = Servicio_video_llamadas

    def set_Nivel_de_satisfacción(self, Nivel_de_satisfacción):
        self.__Nivel_de_satisfacción = Nivel_de_satisfacción

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def get_Servicio_video_llamadas(self):
        return self.__Servicio_video_llamadas

    def get_Nivel_de_satisfacción(self):
        return self.__Nivel_de_satisfacción

    def consultarEncuesta(self):
        return f"edad: {self.__edad} sexo: {self.__sexo} Servicio_video_llamadas: {self.__Servicio_video_llamadas} Nivel_de_satisfacción: {self.__Nivel_de_satisfacción}"


def main():
    N = int(input("Ingresar la cantidad de encuestas realizadas (N): "))
    if not (15 < N < 75):
        main()
        return
    encuestas= []
    sexo = ["M", "F"]
    Servicio_video_llamadas = ["Skype", "Discord", "Zoom"]
    Nivel_de_satisfacción = ["Bajo", "Regular", "Bueno"]
    for i in range(N):
        encuestas.append(CEncuesta(
            sexo[random.randint(0, 1)],
            Servicio_video_llamadas[random.randint(0, 2)],
            Nivel_de_satisfacción [random.randint(0, 2)],
            random.randint(1, 100)
        ))

    personas_mayores_de_60 = 0
    for encuesta in encuestas:
        if encuesta.get_edad() > 60:
            personas_mayores_de_60 += 1
            print(encuesta.consultarEncuesta())
    print(f"Personas mayores de 60: {personas_mayores_de_60}")

    contador_frecuencia = {
        "Skype": 0,
        "Discord": 0,
        "Zoom": 0
    }
    edad = 0
    for encuesta in  encuestas:
        if encuesta.get_Servicio_video_llamadas() == "Skype":
            contador_frecuencia["Skype"] += 1
            edad += encuesta.get_edad()
        if encuesta.get_Servicio_video_llamadas() == "Discord":
            contador_frecuencia["Discord"] += 1
        if encuesta.get_Servicio_video_llamadas() == "Zoom":
            contador_frecuencia["Zoom"] += 1

    print(
        f"Promedio de edad de los Encuestado  de las mujeres que utilizan Zoom.: {edad / contador_frecuencia['Zoom']}")

    menor_frecuencia = contador_frecuencia["Skype"]
    grupo_menor_frecuencia = "Skype"
    for Servicio_video_llamadas in contador_frecuencia:
        if contador_frecuencia[Servicio_video_llamadas] < menor_frecuencia:
            menor_frecuencia = contador_frecuencia[Servicio_video_llamadas]
            Servicio_video_llamadas = Servicio_video_llamadas

    print(f"Grupo con menor frecuencia: {Servicio_video_llamadas} con {menor_frecuencia}")

    edad_Skype = -1
    for encuesta in encuesta:
        if encuesta.get_sexo() == 'F':
            if encuesta.get_grupo() != "Big Data":
                if encuesta.get_edad() >  edad_Skype:
                     edad_Skype = encuesta.get_edad()

    print( edad_Skype == -1 and "No hay hombre más viejo que utiliza Skype" or f"Edad de la mujer que no utiliza skype: {edad_Skype}")
main()
#PREGUNTA 4 - TEMA A
#-*- coding: 1252 *
import random
import matplotlib.pyplot as plt
import pandas as pd


def main():
    gastos = []
    for i in range(24):
        gastos.append(random.randint(0, 1000))

    ingresos = []
    for i in range(24):
        ingresos.append(random.randint(10, 3000))

    grafica = pd.DataFrame({'Gastos': gastos, 'Ingresos': ingresos})
    grafica.plot(title='Evolución de ingresos y gastos')
    plt.show()


main()
