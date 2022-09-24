def llenarArray ():
    numeros = []
    for i in range(2):
        numero = int(input("Digita un numero entero: "))
        numeros.append(numero)
    return numeros

numeros = llenarArray()

def sumar(numeros):
    operacion = 0
    # print(numeros)
    for i in numeros:
        operacion += i
    return(operacion)    
         
sumar(numeros)

# longitud = numeros.count

# def dividir(longitud,operacion):
#     divisor = operacion / longitud
   
#     print(divisor)

# dividir(longitud)        

    