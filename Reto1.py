def llenarArray ():
    numeros = []
    for i in range(2):
        numero = int(input("Digita un numero entero: "))
        numeros.append(numero)
    return numeros

def sumarNumeros(numeros):
    for i in range (numeros):
        suma += i
    return suma

def calcularPromedio(suma,numeros):
    cantNumeros = numeros.count
    promedio = suma/cantNumeros
    print(f'El promedio de los numeros es de: {promedio}')
numeros = llenarArray()
suma = sumarNumeros(numeros)
calcularPromedio(suma,numeros)
