"""
Aluno: Lucas Freire MotaSistema de entrada e saída de produtos usando listas e dicionários.
"""

# LISTA GLOBAL DE PRODUTOS NO ESTOQUE
estoque = []

# LISTA DE PEDIDOS REALIZADOS (SAÍDA)
pedidos = []


# -------------------------------------------------------------------
# FUNÇÃO: Verificar se o produto já existe (por código ou nome)
# -------------------------------------------------------------------
def produto_existe(codigo, nome):
    for item in estoque:
        if item["codigo"] == codigo or item["nome"].lower() == nome.lower():
            return item
    return None


# -------------------------------------------------------------------
# FUNÇÃO: Entrada de Produtos (cadastrar 10 produtos)
# -------------------------------------------------------------------
def entrada_produtos():
    print("\n=== ENTRADA DE PRODUTOS ===")

    for i in range(10):
        print(f"\nCadastro {i+1}/10")

        codigo = input("Código do produto: ")
        nome = input("Nome do produto: ")

        # Verifica duplicidade
        existente = produto_existe(codigo, nome)
        if existente:
            print("Produto já cadastrado. Quantidade será atualizada.")
            qtd = int(input("Quantidade a adicionar: "))
            existente["quantidade"] += qtd
            continue

        # Dados do novo produto
        data_fabricacao = input("Data de fabricação: ")
        fornecedor = input("Fornecedor: ")
        quantidade = int(input("Quantidade inicial: "))
        local = input("Local no estoque: ")
        valor_unitario = float(input("Valor unitário (R$): "))

        produto = {
            "codigo": codigo,
            "nome": nome,
            "data_fabricacao": data_fabricacao,
            "fornecedor": fornecedor,
            "quantidade": quantidade,
            "local": local,
            "valor_unitario": valor_unitario
        }

        estoque.append(produto)
        print("Produto cadastrado com sucesso!")


# -------------------------------------------------------------------
# FUNÇÃO: Saída de Produtos (até 10 pedidos)
# -------------------------------------------------------------------
def saida_produtos():
    print("\n=== SAÍDA DE PRODUTOS ===")

    for i in range(10):
        print(f"\nPedido {i+1}/10")

        cod_pedido = input("Código do pedido: ")
        nome_prod = input("Nome do produto solicitado: ")
        cliente = input("Nome do cliente: ")
        qtd_solicitada = int(input("Quantidade solicitada: "))

        # Buscar produto no estoque
        produto = None
        for item in estoque:
            if item["nome"].lower() == nome_prod.lower():
                produto = item
                break

        if not produto:
            print("Produto não encontrado no estoque!")
            continue

        # Verificar quantidade disponível
        if produto["quantidade"] <= 0:
            print("Produto sem estoque!")
            continue

        # Verificar se quantidade é suficiente
        if qtd_solicitada > produto["quantidade"]:
            print("Estoque insuficiente! Pedido parcialmente atendido.")
            qtd_atendida = produto["quantidade"]
        else:
            qtd_atendida = qtd_solicitada

        # Atualizar estoque
        produto["quantidade"] -= qtd_atendida

        total = qtd_atendida * produto["valor_unitario"]

        # Registrar pedido
        pedido = {
            "codigo_pedido": cod_pedido,
            "cliente": cliente,
            "produto": produto["nome"],
            "quantidade": qtd_atendida,
            "total": total
        }

        pedidos.append(pedido)

        print(f"Pedido registrado! Quantidade atendida: {qtd_atendida}")


# -------------------------------------------------------------------
# Relatório final somente do estoque e pedidos
# -------------------------------------------------------------------
def relatorio():
    print("\n=== RELATÓRIO FINAL ===")

    print("\n--- ESTOQUE (ORDENADO POR NOME) ---")
    lista_ordenada = sorted(estoque, key=lambda x: x["nome"].lower())

    for p in lista_ordenada:
        print("------------------------")
        print(f"Produto: {p['nome']}")
        print(f"Código: {p['codigo']}")
        print(f"Quantidade: {p['quantidade']}")
        print(f"Local: {p['local']}")
        print(f"Valor Unitário: R$ {p['valor_unitario']:.2f}")

    print("\n--- PEDIDOS REALIZADOS ---")
    for ped in pedidos:
        print("------------------------")
        print(f"Pedido: {ped['codigo_pedido']}")
        print(f"Cliente: {ped['cliente']}")
        print(f"Produto: {ped['produto']}")
        print(f"Quantidade: {ped['quantidade']}")
        print(f"Total: R$ {ped['total']:.2f}")
