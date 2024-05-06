def encontrarNPrimos(n):
    lista = []
    numero = 2
    while len(lista) < n:
        primo = True
        divisor = 2
        while divisor < numero:
            if numero % divisor == 0:
                primo = False
            divisor += 1

        if primo:
            lista.append(numero)
        numero += 1
    return lista

n = int(input("Cantidad requerida de N° primos: "))
primos = encontrarNPrimos(n)
print(f"Los primeros {n} números primos son: {primos}")
