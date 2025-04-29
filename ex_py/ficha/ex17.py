print("Multiplos de 5 que nao sao multiplos de 3 :")

numero = 1
while numero <= 1000:
    if numero % 5 == 0 and numero % 3 != 0:
        print(numero, end=' ')
    numero += 1
