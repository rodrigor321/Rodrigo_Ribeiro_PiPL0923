soma = 0
contador = 0

for i in range(30):
    while True:
        try:
            numero = int(input(f"Escreve o {i+1}º numero par : "))
            
            if 1 <= numero <= 50:
                if numero % 2 == 0:
                    soma += numero
                    break
                else:
                    print("O numero não é par.")
            else:
                print("O numero esta fora do intervalo permitido")
        except ValueError:
            print("Numero inteiros apenas")

media = soma / 30
print(f"\nA media dos 30 numeros pares e: {media:.2f}")
