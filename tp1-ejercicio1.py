print("Inicio trabajo practico 1")

# Solicitar números al usuario
numero1 = int(input("Introduce la base/radicando: "))
numero2 = int(input("Introduce el exponente/indice: "))


def potencia(base, exponente):
    if exponente == 0:
        return 1    
    elif exponente < 0:
        return 1 / (potencia(base, -exponente))
    elif exponente % 2 != 0:
        return potencia(base, exponente - 1) * base
    elif exponente % 2 == 0:
        y = potencia(base, exponente / 2)
        return y * y


def raiz(radicando, indice):
    if indice > 1:
        for i in range(radicando):
            if potencia(i, indice) == radicando:
                return i
    elif indice == 1:
        return radicando
    else:
        return 0


# Imprimir los números introducidos por el usuario
print("Resultado potencia: ", potencia(numero1, numero2))
if raiz(numero1, numero2) == 0 or (raiz(numero1, numero2) == None) :
    print("No hay solución en Z para la raíz")
else:
    print("la raiz ", numero2, "° de ", numero1, " es: ", raiz(numero1, numero2))
