def calcular_desconto(valor_compra):
    if 100 <= valor_compra <= 200:
        return valor_compra * 0.05
    elif 200 < valor_compra < 500:
        return valor_compra * 0.10
    elif valor_compra >= 500:
        return valor_compra * 0.15
    return 0

def adicionar_cliente(lista_clientes, id_cliente):
    nome_cliente = input("Nome do cliente: ")
    endereco_cliente = input("Endereco do cliente: ")
    telefone_cliente = input("Telefone do cliente: ")
    nif_cliente = input("NIF do cliente: ")
    valor_compra = float(input("Valor da compra: "))
    
    desconto_cliente = calcular_desconto(valor_compra)
    divida_final = valor_compra - desconto_cliente
    
    cliente = {
        "id_cliente": id_cliente,
        "nome_cliente": nome_cliente,
        "endereco_cliente": endereco_cliente,
        "telefone_cliente": telefone_cliente,
        "nif_cliente": nif_cliente,
        "valor_compra": valor_compra,
        "desconto_cliente": desconto_cliente,
        "divida_final": divida_final
    }
    
    lista_clientes.append(cliente)
    print(f"Cliente {nome_cliente} adicionado com sucesso!")

def exibir_informacoes_cliente(cliente):
    print(f"\nID Cliente: {cliente['id_cliente']}")
    print(f"Nome: {cliente['nome_cliente']}")
    print(f"Endereco: {cliente['endereco_cliente']}")
    print(f"Telefone: {cliente['telefone_cliente']}")
    print(f"NIF: {cliente['nif_cliente']}")
    print(f"Valor da Compra: {cliente['valor_compra']}")
    print(f"Desconto: {cliente['desconto_cliente']}")
    print(f"Divida Final: {cliente['divida_final']}")

def listar_todos_clientes(lista_clientes):
    if not lista_clientes:
        print("Nao ha clientes para listar.")
        return

    for idx, cliente in enumerate(lista_clientes):
        exibir_informacoes_cliente(cliente)
        if idx < len(lista_clientes) - 1:  
            continuar = input("Pressione Enter para continuar para o proximo cliente ou 'S' para parar: ")
            if continuar.lower() == 's':
                break

def buscar_cliente_por_id(lista_clientes, id_cliente_busca):
    for cliente in lista_clientes:
        if cliente["id_cliente"] == id_cliente_busca:
            exibir_informacoes_cliente(cliente)
            return
    print("Cliente nao encontrado!")

def menu():
    lista_clientes = []  
    id_cliente = 1    

    while True:
        print("\nMenu de Opcoes:")
        print("1. Adicionar cliente")
        print("2. Listar todos os clientes")
        print("3. Buscar cliente por ID")
        print("4. Sair")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == '1':
            adicionar_cliente(lista_clientes, id_cliente)
            id_cliente += 1  
        elif opcao == '2':
            listar_todos_clientes(lista_clientes)
        elif opcao == '3':
            id_cliente_busca = int(input("Digite o ID do cliente para busca: "))
            buscar_cliente_por_id(lista_clientes, id_cliente_busca)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida! Tente novamente.")

menu()
