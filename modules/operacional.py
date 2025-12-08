
import json
import os

# Configuração do diretório de dados
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
    
    for dia in dias_semana:
        print(f"\nDia: {dia}")
        producao_dia = {"dia": dia, "turnos": {}}
        
        for turno in turnos:
            while True:
                try:
                    qtd = int(input(f"  Produção Turno {turno}: "))
                    if qtd < 0:
                        print("    Erro: A quantidade não pode ser negativa.")
                        continue
                    
                    producao_dia["turnos"][turno] = qtd
                    
                    # Adiciona ao formato flat para salvar
                    dados_flat.append({
                        "dia": dia,
                        "turno": turno,
                        "quantidade": qtd
                    })
                    break
                except ValueError:
                    print("    Erro: Digite um número inteiro válido.")
        
        producao_semanal.append(producao_dia)
    
    # Salvar dados
    try:
        # Carregar dados existentes se houver
        dados_existentes = []
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                dados_existentes = json.load(f)
        
        # Adicionar novos dados
        dados_existentes.extend(dados_flat)
        
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
        
    Cálculos:
        - Total Semanal = Σ todas produções
        - Média Diária = Total Semanal / 7
        - Média por Turno = Total do Turno / 7
    """
    total_semanal = 0
    total_por_turno = {"Manhã": 0, "Tarde": 0, "Noite": 0}
    
    for dia_data in dados:
        for turno, qtd in dia_data["turnos"].items():
            total_semanal += qtd
            total_por_turno[turno] += qtd
            
    media_diaria = total_semanal / 7
    
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
        
    Fórmulas:
        - Mensal = Total Semanal × 4
        - Anual = Total Semanal × 52
    """
    mensal = total_semanal * 4
    anual = total_semanal * 52
    return mensal, anual

def calcular_capacidade_ideal():
    """
    Calcula a produção ideal com 100% da capacidade.
    Capacidade padrão: 500 unidades/mês com 2 turnos.
    Terceiro turno aumenta 50%.
    
    Returns:
        dict: {
            'semanal': float,  # 187.5 unidades
            'mensal': float,   # 750 unidades
            'anual': float     # 9000 unidades
        }
        
    Premissas:
        - Capacidade base (2 turnos): 500/mês
        - Com 3 turnos: 750/mês (+50%)
    """
    # Capacidade base é 500/mês (2 turnos)
    # Com 3 turnos aumenta 50% => 750/mês
    cap_mensal = 750
    cap_semanal = cap_mensal / 4
    cap_anual = cap_mensal * 12
    
    return {
        "semanal": cap_semanal,
        "mensal": cap_mensal,
        "anual": cap_anual
    }

def gerar_relatorio(dados, estatisticas, ideal):
    """
    Emite um relatório comparativo entre produção real e ideal.
    
    Args:
        dados (list): Dados de produção
        estatisticas (dict): Estatísticas calculadas
        ideal (dict): Capacidade ideal
        
    Side Effects:
        Imprime relatório formatado com:
        - Produção total e médias
        - Simulações mensal/anual
        - Comparativo com capacidade ideal
        - Diferenças (gaps) de produção
    """
    sim_mensal, sim_anual = simular_producao(estatisticas["total_semanal"])
    
    print("\n" + "="*50)
    print("RELATÓRIO OPERACIONAL SEMANAL")
    print("="*50)
    
    print(f"\n📊 PRODUÇÃO REAL:")
    print(f"  • Total Semanal: {estatisticas['total_semanal']} unidades")
    print(f"  • Média Diária:  {estatisticas['media_diaria']:.1f} unidades")
    
    print("\n🔄 POR TURNO (MÉDIA/DIA):")
    for turno, media in estatisticas["media_por_turno"].items():
        print(f"  • {turno:<6}: {media:.1f} un")
        
    print("\n🔮 PROJEÇÕES:")
    print(f"  • Mensal: {sim_mensal} un")
    print(f"  • Anual:  {sim_anual} un")
    
    print("\n🎯 COMPARATIVO COM IDEAL (3 TURNOS):")
    print(f"  • Meta Semanal: {ideal['semanal']:.1f} un")
    print(f"  • Realizado:    {estatisticas['total_semanal']} un")
    
    diff = estatisticas['total_semanal'] - ideal['semanal']
    status = "ACIMA DA META" if diff >= 0 else "ABAIΧΟ DA META"
    cor = "✅" if diff >= 0 else "⚠️"
    
    print(f"\n  STATUS: {cor} {status}")
    print(f"  Diferença: {diff:+.1f} unidades")
    print("="*50 + "\n")

if __name__ == "__main__":
    # Teste rápido se executado diretamente
    print("Iniciando módulo operacional (Modo Teste)...")
    dados = cadastrar_producao()
    stats = calcular_estatisticas(dados)
    ideal = calcular_capacidade_ideal()
    gerar_relatorio(dados, stats, ideal)
