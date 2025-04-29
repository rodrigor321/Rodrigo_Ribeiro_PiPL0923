n = int(input("Introduza um numero inteiro positivo: "))
quantidade_perfeitos = 0

for i in range(1, n + 1):
    soma_divisores = 0
    for j in range(1, i):
        if i % j == 0:
            soma_divisores += j
    if soma_divisores == i:
        print(f"{i} é um numero perfeito.")
        quantidade_perfeitos += 1

print(f"\nQuantidade de numeros perfeitos entre 1 e {n}: {quantidade_perfeitos}")
