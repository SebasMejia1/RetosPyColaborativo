def llenarArray ():
    numeros = []
    for i in range(10):
        numero = int(input("Digita un numero entero: "))
        numeros.append(numero)
    return numeros

def sumarNumeros(numeros):
    suma = 0
    for i in range (len(numeros)):
        suma += numeros[i]
    return suma

def calcularPromedio(suma,numeros):
    cantNumeros = len(numeros)
    promedio = suma/cantNumeros
    print(f'El promedio de los numeros es de: {promedio}')
    
numeros = llenarArray()
suma = sumarNumeros(numeros)
calcularPromedio(suma,numeros)
