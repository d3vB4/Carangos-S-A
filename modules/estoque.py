"""
Módulo: Estoque
Descrição: Gerencia cadastro, busca e custos de produtos.
Refatorado para integração com DataManager e MVC do main.py.
"""

import json
import os

try:
    from modules import data_manager
except ImportError:
    import data_manager

FILE_NAME = 'produtos.json'

def cadastrar_produto(codigo, nome, data_fab, fornecedor, quantidade, valor_compra):
    """
    Cadastra um novo produto no sistema.
    Argumentos recebidos do main.py.
    """
    print(f"\n--- Processando Cadastro: {nome} ---")
    
    produtos = data_manager.load_data(FILE_NAME)
    
    # Verifica duplicidade por código
    for p in produtos:
        if str(p['codigo']) == str(codigo):
            print(f"Erro: Produto com código {codigo} já existe!")
            return False

    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "data_fabricacao": data_fab,
        "fornecedor": fornecedor,
        "quantidade": quantidade,
        "valor_compra": valor_compra,
        # Campos extras calculados ou padrão
        "valor_total": quantidade * valor_compra
    }
    
    produtos.append(novo_produto)
    
    if data_manager.save_data(FILE_NAME, produtos):
        print("Produto cadastrado com sucesso!")
        return True
    else:
        print("Erro ao salvar produto.")
        return False

def pesquisar_produto(termo):
    """
    Pesquisa produtos por nome ou código.
    Retorna uma lista de dicionários encontrados.
    """
    produtos = data_manager.load_data(FILE_NAME)
    resultados = []
    
    termo = str(termo).lower()
    
    for p in produtos:
        if termo in str(p['codigo']).lower() or termo in p['nome'].lower():
            resultados.append(p)
            
    return resultados

def calcular_custos(produtos=None):
    """
    Calcula custos totais e projeções.
    Se produtos for None, carrega do arquivo.
    """
    if produtos is None:
        produtos = data_manager.load_data(FILE_NAME)
        
    total_atual = sum(p['quantidade'] * p['valor_compra'] for p in produtos)
    
    # Lógica simples de projeção (Exemplo: Manutenção custa 10% a.m do valor do estoque)
    mensal_projetado = total_atual * 0.10
    anual_projetado = mensal_projetado * 12
    
    return {
        "total_atual": total_atual,
        "mensal_projetado": mensal_projetado,
        "anual_projetado": anual_projetado
    }
