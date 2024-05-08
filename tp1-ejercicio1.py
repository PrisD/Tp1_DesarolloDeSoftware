print("Inicio trabajo practico 1")
numero1 = int(input("Introduce la base/radicando: "))
numero2 = int(input("Introduce el exponente/indice: "))


def potencia(base, exponente):
    resultado = 0
    if exponente == 0:
        resultado = 1    
    elif exponente < 0:
        resultado = 1 / (potencia(base, -exponente))
    elif exponente % 2 != 0:
        resultado = potencia(base, exponente - 1) * base
    elif exponente % 2 == 0:
        y = potencia(base, exponente / 2)
        resultado = y * y
    return resultado


def raiz(radicando, indice):
    resultado = 0
    if indice > 1:
        for i in range(radicando):
            if potencia(i, indice) == radicando:
                resultado = i
    elif indice == 1:
        resultado = radicando
    else:
        resultado = 0
    return resultado


print("Resultado potencia: ", potencia(numero1, numero2))
if raiz(numero1, numero2) == 0 or (raiz(numero1, numero2) == None) :
    print("No hay solución en Z para la raíz")
else:
    print("la raiz ", numero2, "° de ", numero1, " es: ", raiz(numero1, numero2))
