def encontrarNPrimos(n):
    lista = []
    numero = 2
    while len(lista) < n:
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
        if primo:
            lista.append(numero)
        numero += 1
    return lista


# Ejemplo de uso
n = int(input("Cuantos nro primos queres ??"))
primos = encontrarNPrimos(n)
print(f"Los primeros {n} números primos son: {primos}")
