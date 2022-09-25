def recibirDatos ():
    ancho = int(input("Digite el ancho: "))
    alto = int(input("Digite el alto: "))
    datos = [ancho,alto]
    return datos

def calcularArea(ancho,alto):
    area = (ancho*alto)/2
    return area

def calcularPerimetro(ancho,alto):
    perimetro = (ancho*2)+(alto*2)

def graficar(ancho,alto):  
   for i in range(alto):
    for j in range(ancho):
        print("* ", end="")
    print()
datos = recibirDatos()
ancho = datos[0]
alto = datos[1]
graficar(ancho, alto)

