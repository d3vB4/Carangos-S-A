
# Nome: Alexandre Calmon
# Módulo: Operacional
# Descrição: Gerencia cadastro de produção e estatísticas operacionais.

import json
import os

# Configuração do diretório de dados
# O módulo utiliza uma variável de ambiente ou default para flexibilidade em diferentes ambientes (dev/prod)
DATA_DIR = os.getenv("DATA_DIR", "data")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

DATA_FILE = os.path.join(DATA_DIR, "producao.json")

def cadastrar_producao():
    """
    Cadastra a produção diária de cada turno por 7 dias.
    Retorna uma lista de dicionários com os dados.
    
    Returns:
        list: Lista com dados de produção semanal estruturados por dia e turno
        
    Estrutura de Entrada:
        - 7 dias da semana
        - 3 turnos por dia (Manhã, Tarde, Noite)
        
    Side Effects:
        - Solicita input do usuário para cada turno
        - Valida entrada numérica
        - Converte dados para formato flat
        - Salva em 'producao.json'
        - Append aos dados existentes
    """
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    turnos = ["Manhã", "Tarde", "Noite"]
    
    producao_semanal = []
    dados_flat = []
    
    print("\n=== Cadastro de Produção Semanal ===")
    
    # Itera sobre cada dia da semana para coletar dados completos
    for dia in dias_semana:
        print(f"\nDia: {dia}")
        producao_dia = {"dia": dia, "turnos": {}}
        
        # Para cada dia, coleta dados dos 3 turnos
        for turno in turnos:
            while True:
                try:
                    # Input interativo protegido por try/except para garantir números inteiros
                    qtd = int(input(f"  Produção Turno {turno}: "))
                    
                    # Regra de negócio: produção não pode ser negativa
                    if qtd < 0:
                        print("    Erro: A quantidade não pode ser negativa.")
                        continue
                    
                    producao_dia["turnos"][turno] = qtd
                    
                    # Prepara estrutura plana (flat) para facilitar análise futura ou exportação CSV/BD
                    dados_flat.append({
                        "dia": dia,
                        "turno": turno,
                        "quantidade": qtd
                    })
                    break
                except ValueError:
                    print("    Erro: Digite um número inteiro válido.")
        
        producao_semanal.append(producao_dia)
    
    # Persistência dos dados
    try:
        # Tenta carregar dados antigos para não sobrescrever histórico
        dados_existentes = []
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                dados_existentes = json.load(f)
        
        # Concatena novos dados
        dados_existentes.extend(dados_flat)
        
        # Salva o arquivo atualizado com indentação para legibilidade humana
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(dados_existentes, f, indent=4, ensure_ascii=False)
            
        print(f"\n✅ Dados de produção salvos em {DATA_FILE}")
        
    except Exception as e:
        print(f"\n❌ Erro ao salvar dados: {e}")
        
    return producao_semanal

def calcular_estatisticas(dados):
    """
    Calcula produção total semanal, média por dia e por turno.
    Retorna um dicionário com as estatísticas.
    
    Args:
        dados (list): Lista de dicionários com produção por dia/turno
        
    Returns:
        dict: {
            'total_semanal': int,
            'media_diaria': float,
            'media_por_turno': dict,  # {turno: média}
            'total_por_turno': dict   # {turno: total}
        }
    """
    total_semanal = 0
    total_por_turno = {"Manhã": 0, "Tarde": 0, "Noite": 0}
    
    # Itera pelos dados estruturados para somar totais
    for dia_data in dados:
        for turno, qtd in dia_data["turnos"].items():
            total_semanal += qtd
            total_por_turno[turno] += qtd
            
    # Cálculo de médias simples (considerando 7 dias fixos)
    media_diaria = total_semanal / 7
    
    # Dictionary comprehension para calcular média de cada turno
    media_por_turno = {
        turno: total / 7 
        for turno, total in total_por_turno.items()
    }
    
    return {
        "total_semanal": total_semanal,
        "media_diaria": media_diaria,
        "media_por_turno": media_por_turno,
        "total_por_turno": total_por_turno
    }

def simular_producao(total_semanal):
    """
    Simula a produção mensal e anual com base na produção semanal.
    Args:
        total_semanal (int): Total produzido na semana
    Returns:
        tuple: (mensal, anual)
    """
    # Projeção linear simples: Mês comercial de 4 semanas, Ano de 52 semanas
    mensal = total_semanal * 4
    anual = total_semanal * 52
    return mensal, anual

def calcular_capacidade_ideal(meta_mensal=None):
    """
    Calcula a produção ideal com base em uma meta definida pelo usuário.
    Se nenhuma meta for passada, solicita input interativo.
    
    Args:
        meta_mensal (float, optional): Meta mensal pré-definida. Se None, pede ao usuário.
        
    Returns:
        dict: {
            'semanal': float,
            'mensal': float,
            'anual': float
        }
    """
    # Permite que o usuário defina sua própria meta (requisito: "quero eu mesmo setar")
    if meta_mensal is None:
        try:
            print("\n=== Configuração de Metas ===")
            entrada = input("Digite a meta de produção MENSAL desejada (Ex: 750): ")
            meta_mensal = float(entrada)
            if meta_mensal <= 0:
                print("⚠️ Meta inválida ou zero. Usando padrão de 750 un.")
                meta_mensal = 750
        except ValueError:
            print("⚠️ Valor inválido. Usando padrão de 750 un.")
            meta_mensal = 750
            
    # Deriva as outras metas a partir da mensal
    meta_semanal = meta_mensal / 4
    meta_anual = meta_mensal * 12
    
    return {
        "semanal": meta_semanal,
        "mensal": meta_mensal,
        "anual": meta_anual
    }

def gerar_relatorio(dados, estatisticas, ideal):
    """
    Emite um relatório executivo com insights detalhados.
    
    Args:
        dados (list): Média bruta
        estatisticas (dict): Dados processados
        ideal (dict): Metas
    """
    sim_mensal, sim_anual = simular_producao(estatisticas["total_semanal"])
    
    print("\n" + "="*60)
    print("📋 RELATÓRIO OPERACIONAL EXECUTIVO - INSIGHTS")
    print("="*60)
    
    # Seção 1: Dados Reais
    print(f"\n📊 PRODUÇÃO REAL:")
    print(f"  • Total Semanal: {estatisticas['total_semanal']} unidades")
    print(f"  • Média Diária:  {estatisticas['media_diaria']:.1f} unidades")
    
    # Seção 2: Desempenho por Turno
    print("\n🔄 PERFORMANCE POR TURNO:")
    # Identifica o melhor turno para insight
    melhor_turno = max(estatisticas["media_por_turno"], key=estatisticas["media_por_turno"].get)
    pior_turno = min(estatisticas["media_por_turno"], key=estatisticas["media_por_turno"].get)
    
    for turno, media in estatisticas["media_por_turno"].items():
        destaque = "⭐ (Melhor)" if turno == melhor_turno else ""
        print(f"  • {turno:<6}: {media:.1f} un/dia {destaque}")
        
    # Seção 3: Comparativo e Insights
    print("\n🎯 ANÁLISE DE METAS E INSIGHTS:")
    print(f"  • Meta Semanal (Definida): {ideal['semanal']:.1f} un")
    print(f"  • Realizado:               {estatisticas['total_semanal']} un")
    
    # Cálculo de eficiência
    eficiencia = (estatisticas['total_semanal'] / ideal['semanal']) * 100
    diff = estatisticas['total_semanal'] - ideal['semanal']
    
    status = "ACIMA DA META" if diff >= 0 else "ABAIΧΟ DA META"
    cor = "✅" if diff >= 0 else "⚠️"
    
    print(f"\n  STATUS: {cor} {status}")
    print(f"  Eficiência: {eficiencia:.1f}% da meta")
    print(f"  Diferença:  {diff:+.1f} unidades")
    
    # Seção 4: Recomendações Automáticas (Insights Avançados)
    print("\n💡 INSIGHTS E RECOMENDAÇÕES:")
    if eficiencia >= 100:
        print("  ✅ A equipe está com excelente desempenho! Considere aumentar a meta mensal.")
    elif eficiencia >= 80:
        print("  ⚠️ A meta está próxima. Foque no turno com menor desempenho para alcançar 100%.")
    else:
        print("  ❌ Desempenho crítico. É necessário rever processos ou verificar ausências.")
        
    print(f"  👉 Dica: O turno '{pior_turno}' tem o menor rendimento. Investigue gargalos neste horário.")

    print("="*60 + "\n")

if __name__ == "__main__":
    # Teste rápido interativo
    print("Iniciando módulo operacional (Modo Teste)...")
    dados = cadastrar_producao()
    stats = calcular_estatisticas(dados)
    # Agora a capacidade pede input se não passar argumento
    ideal = calcular_capacidade_ideal() 
    gerar_relatorio(dados, stats, ideal)
