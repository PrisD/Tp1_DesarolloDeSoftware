ingreso = int(input("Ingresa un número: "))
listaPositivos =[]
listaNegativos =[]

while ingreso != 0 :
    if ingreso < 0:
        listaNegativos.append(ingreso)
    else:
        listaPositivos.append(ingreso)
    ingreso = int(input("Ingresa un número: "))


def extremosEnLista(listaNumeros):
    alto = listaNumeros[0]
    bajo = listaNumeros[0]

    for numero in listaNumeros:
        if numero > alto:
            alto = numero
        elif numero < bajo:
            bajo = numero

    return (alto, bajo)

resultadoPositivos = extremosEnLista(listaPositivos)
resultadoNegativos= extremosEnLista(listaNegativos)
print("Para la lista de números positivos:")
print(
    f"Número más alto: {resultadoPositivos[0]}, Número más bajo: {resultadoPositivos[1]}"
)

print("Para la lista de números negativos:")
print(
    f"Número más alto: {resultadoNegativos[0]}, Número más bajo: {resultadoNegativos[1]}"
)
