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


n = int(input("Cantidad requerida de N° primos: "))
primos = encontrarNPrimos(n)
print(f"Los primeros {n} números primos son: {primos}")
