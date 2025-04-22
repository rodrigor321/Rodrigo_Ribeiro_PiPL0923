nomes = []
def menu():
    print("1 - Introduzir nomes na lista")
    print("2 - Listar os nomes da lista")
    print("3 - Parar programa")
while True:
    menu()
    opcao = input("Escolha uma opção 1, 2, 3: ")
    match opcao:
        case "1":
            nome = input("Introduza um nome: ")
            nomes.append(nome)
        case "2":
            if nomes:
                print("Lista de Nomes:")
                for nome in nomes:
                    print(nome)
            else:
                print("A lista esta sem nada")
        case "3":
            print("Programa fechado")
            break
        case _:
            print("Opção inválida")
