ingreso = int(input("Ingresa un número: "))
listaPositivos =[]
listaNegativos =[]

while ingreso != 0 :
    if ingreso < 0:
        listaNegativos.append(ingreso)
    else:
        listaPositivos.append(ingreso)
    ingreso = int(input("Ingresa un número: "))


def numMasAlto(listaNumeros):
    alto = listaNumeros[0]
    for i in range(1, len(listaNumeros)): 
        if alto < listaNumeros[i]:
            alto = listaNumeros[i]
    return alto

def numMasBajo(listaNumeros):
    bajo = listaNumeros[0]
    for i in range(1,len(listaNumeros)):
        if bajo > listaNumeros[i]:
            bajo =listaNumeros[i]
    return bajo


print(listaPositivos)
print(listaNegativos)
print("El más alto de los positivos: ",numMasAlto(listaPositivos))
print("El más alto de los negativos: ", numMasAlto(listaNegativos))
print("El más bajo de los positivos: ", numMasBajo(listaPositivos))
print("El más bajo de los negativos: ", numMasBajo(listaNegativos))
 