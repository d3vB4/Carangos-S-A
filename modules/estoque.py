# Nome: [Seu Nome Aqui]
# Módulo: Estoque
# Descrição: Gerencia produtos, preços e custos de estoque.

try:
    from modules import data_manager
except ImportError:
    import data_manager

def cadastrar_produto(codigo, nome, data_fab, fornecedor, quantidade, valor_compra):
    """
    Cadastra um novo produto na lista de produtos.
    Verifica duplicidade de código antes de inserir.
    
    Args:
        codigo (int): Código único do produto
        nome (str): Nome do produto
        data_fab (str): Data de fabricação (formato: DD/MM/YYYY)
        fornecedor (str): Nome do fornecedor
        quantidade (int): Quantidade em estoque
        valor_compra (float): Valor unitário de compra
        
    Returns:
        bool: True se cadastrou com sucesso, False se código duplicado
    """
    if verificar_duplicidade(codigo):
        print(f"Erro: Produto com código {codigo} já existe.")
        return False
        
    produtos = data_manager.load_data('produtos.json')
    
    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "data_fabricacao": data_fab,
        "fornecedor": fornecedor,
        "quantidade": quantidade,
        "valor_compra": valor_compra
    }
    
    produtos.append(novo_produto)
    
    if data_manager.save_data('produtos.json', produtos):
        print(f"Produto {nome} cadastrado com sucesso!")
        return True
    return False

def verificar_duplicidade(codigo):
    """
    Verifica se já existe um produto com o código informado.
    Retorna True se existir, False caso contrário.
    """
    produtos = data_manager.load_data('produtos.json')
    for p in produtos:
        if p.get('codigo') == codigo:
            return True
    return False

def pesquisar_produto(termo):
    """
    Pesquisa produto por nome ou código.
    Retorna uma lista de produtos encontrados.
    """
    produtos = data_manager.load_data('produtos.json')
    resultados = []
    
    termo_str = str(termo).lower()
    
    for p in produtos:
        if termo_str in str(p.get('codigo')) or termo_str in p.get('nome', '').lower():
            resultados.append(p)
            
    return resultados

def calcular_custos(lista_produtos=None):
    """
    Calcula o custo total do estoque (semanal, mensal, anual).
    Aceita uma lista opcional de produtos. Se não fornecida, usa a global.
    
    Returns:
        dict: {
            'total_atual': float,      # Custo total atual (semanal)
            'mensal_projetado': float, # Projeção mensal (x4)
            'anual_projetado': float   # Projeção anual (x52)
        }
    """
    if lista_produtos is None:
        lista_produtos = data_manager.load_data('produtos.json')
        
    total_atual = sum(p['quantidade'] * p['valor_compra'] for p in lista_produtos)
    
    return {
        'total_atual': total_atual,
        'mensal_projetado': total_atual * 4,
        'anual_projetado': total_atual * 52
    }

def listar_produtos():
    """
    Lista todos os produtos cadastrados.
    """
    produtos = data_manager.load_data('produtos.json')
    print("\n--- Lista de Produtos ---")
    for p in produtos:
        print(f"#{p['codigo']} - {p['nome']} (Qtd: {p['quantidade']} | R$ {p['valor_compra']:.2f})")
