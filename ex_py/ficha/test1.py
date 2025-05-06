def verificar_primo(numero: int):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_divisores(numero: int):
    return sum(1 for i in range(1, numero + 1) if numero % i == 0)

def contar_numeros_perfeitos(limite: int):
    return sum(1 for i in range(1, limite + 1) if sum(n for n in range(1, i) if i % n == 0) == i)

numero = int(input("Introduza um numero: "))
contador = 0

while contador < numero:
    i = numero - contador
    if contador % 10 == 0 and contador != 0:
        resposta = input("Deseja continuar? S ou N: ")
        if resposta.upper() == 'N':
            break
    
    divisores = contar_divisores(i)
    perfeitos = contar_numeros_perfeitos(i)
    primo = "e primo" if verificar_primo(i) else "nao e primo"
    
    print(f"O numero {i}, tem {divisores} divisores, tem {perfeitos} numeros perfeitos, {primo}.")
    
    contador += 1

while True:
    operacoes = "+-*/."
    print("\nCalculadora")
    print("\t+")
    print("\t-")
    print("\t*")
    print("\t/")    
    print("\t. - para mostrar a tabuada\n")
    
    operacao = input("Introduza a operacao: ")
    if operacao in operacoes:
        break

if operacao == ".":
    numero_tab = int(input("Introduza o numero para a tabuada: "))
    i = 1
    while i <= 10:
        if i % 20 == 1 and i != 1:
            resposta = input("Deseja continuar? S ou N: ")
            if resposta.upper() == 'N':
                break
        print(f"{numero_tab} x {i} = {numero_tab * i}")
        i += 1
else:
    numero1 = int(input("Introduza o primeiro numero: "))
    numero2 = int(input("Introduza o segundo numero: "))
    
    match operacao:
        case "+":
            resultado = numero1 + numero2
        case "-":
            resultado = numero1 - numero2
        case "*":
            resultado = numero1 * numero2
        case "/":
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                print("Erro: Divisao por zero nao e permitida!")
                resultado = None
        case _:
            print("Operacao invalida!")

    if resultado is not None:
        print(f"{numero1} {operacao} {numero2} = {resultado}")
