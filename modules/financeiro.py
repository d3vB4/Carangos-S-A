# Nome do Aluno: [Seu Nome Aqui]
# Módulo: Financeiro
# Descrição: Gerencia cálculo de custos de água, luz e despesas da fábrica.

# Importa o módulo de gerenciamento de dados (para salvar/carregar arquivos JSON)
try:
    from modules import data_manager  # Tenta importar quando executado como módulo
except ImportError:
    import data_manager  # Importa diretamente quando executado standalone

# Importa módulo RH para usar funções de cálculo de salário
try:
    from modules import rh
except ImportError:
    import rh

# ============================================================================
# FUNÇÕES PARA CÁLCULO DE UTILIDADES DA FÁBRICA (24/7, 30 DIAS)
# ============================================================================

def calcular_custo_agua_fabrica(dias_trabalhados=30):
    """
    Calcula o custo total de água da fábrica no mês.
    
    Regra: R$ 1,50 por hora por trabalhador
    A fábrica opera 24 horas por dia, 30 dias por mês
    
    Exemplo: 5 funcionários × 24h × 30 dias × R$ 1,50 = R$ 5.400,00
    """
    # Carrega a lista de funcionários do arquivo JSON
    funcionarios = data_manager.load_data('funcionarios.json')
    
    # Conta quantos funcionários existem (se não houver, retorna 0)
    qtd_funcionarios = len(funcionarios) if funcionarios else 0
    
    # Se não há funcionários, retorna custo zero
    if qtd_funcionarios == 0:
        return {'tipo': 'Água', 'custo_total': 0, 'qtd_funcionarios': 0}
    
    # Define o custo de água por hora por trabalhador
    custo_por_hora = 1.50  # R$ 1,50 por hora
    
    # Calcula total de horas da fábrica no mês (24h × 30 dias = 720 horas)
    total_horas = 24 * dias_trabalhados
    
    # Calcula o custo total: horas × funcionários × custo por hora
    # Exemplo: 720h × 5 funcionários × R$ 1,50 = R$ 5.400,00
    custo_total = total_horas * qtd_funcionarios * custo_por_hora
    
    # Retorna um dicionário com todos os detalhes do cálculo
    return {
        'tipo': 'Água',
        'custo_por_hora': custo_por_hora,
        'horas_por_dia': 24,
        'dias_trabalhados': dias_trabalhados,
        'qtd_funcionarios': qtd_funcionarios,
        'total_horas': total_horas,
        'custo_total': custo_total
    }

def calcular_custo_luz_fabrica(dias_trabalhados=30):
    """
    Calcula o custo total de energia elétrica da fábrica no mês.
    
    A fábrica usa dois tipos de energia:
    - 8 horas/dia com GERADOR: R$ 1,60 por hora por trabalhador (mais barato)
    - 16 horas/dia na REDE ELÉTRICA: R$ 2,40 por hora por trabalhador (mais caro)
    
    Exemplo com 5 funcionários:
    - Gerador: 8h × 30 dias × 5 × R$ 1,60 = R$ 1.920,00
    - Rede: 16h × 30 dias × 5 × R$ 2,40 = R$ 5.760,00
    - Total: R$ 7.680,00
    """
    # Carrega a lista de funcionários do arquivo JSON
    funcionarios = data_manager.load_data('funcionarios.json')
    
    # Conta quantos funcionários existem
    qtd_funcionarios = len(funcionarios) if funcionarios else 0
    
    # Se não há funcionários, retorna custo zero
    if qtd_funcionarios == 0:
        return {'tipo': 'Energia', 'custo_total': 0, 'qtd_funcionarios': 0}
    
    # CÁLCULO DO CUSTO COM GERADOR (8 horas por dia)
    # Fórmula: 8 horas × 30 dias × quantidade de funcionários × R$ 1,60
    # Exemplo: 8 × 30 × 5 × 1.60 = R$ 1.920,00
    custo_gerador = 8 * dias_trabalhados * qtd_funcionarios * 1.60
    
    # CÁLCULO DO CUSTO COM REDE ELÉTRICA (16 horas por dia)
    # Fórmula: 16 horas × 30 dias × quantidade de funcionários × R$ 2,40
    # Exemplo: 16 × 30 × 5 × 2.40 = R$ 5.760,00
    custo_rede = 16 * dias_trabalhados * qtd_funcionarios * 2.40
    
    # Retorna um dicionário com todos os detalhes do cálculo
    return {
        'tipo': 'Energia',
        'horas_gerador_dia': 8,          # 8 horas por dia com gerador
        'custo_gerador_hora': 1.60,      # R$ 1,60 por hora
        'horas_rede_dia': 16,            # 16 horas por dia na rede
        'custo_rede_hora': 2.40,         # R$ 2,40 por hora
        'dias_trabalhados': dias_trabalhados,
        'qtd_funcionarios': qtd_funcionarios,
        'custo_gerador': custo_gerador,  # Custo total do gerador
        'custo_rede': custo_rede,        # Custo total da rede
        'custo_total': custo_gerador + custo_rede  # Soma dos dois
    }

def calcular_salarios_fabrica(horas_normais=176, horas_extras=10):
    """
    Calcula o custo total de salários usando as funções do módulo RH.
    
    Usa as mesmas regras e cálculos do rh.py:
    - calcular_salario_bruto() - Salário base
    - calcular_horas_extras() - Horas extras (gerentes/diretores não recebem)
    - calcular_irpf() - Imposto de renda
    - calcular_liquido() - Salário líquido
    
    Regras:
    - Horas normais: 176h/mês (8h/dia × 22 dias úteis)
    - Horas extras: 10h/mês (padrão)
    - Hora extra vale 1.5x o valor normal (exceto gerentes/diretores)
    """
    # Carrega a lista de funcionários do arquivo JSON
    funcionarios = data_manager.load_data('funcionarios.json')
    
    # Se não há funcionários, retorna custo zero
    if not funcionarios:
        return {
            'tipo': 'Salários',
            'qtd_funcionarios': 0,
            'custo_total_bruto': 0,
            'custo_total_liquido': 0,
            'total_irpf': 0,
            'detalhes': []
        }
    
    # Lista para armazenar detalhes de cada funcionário
    detalhes_funcionarios = []
    custo_total_bruto = 0
    custo_total_liquido = 0
    total_irpf = 0
    
    # Calcula o salário de cada funcionário usando funções do RH
    for func in funcionarios:
        nome = func.get('nome', 'Sem nome')
        valor_hora = func.get('valor_hora', 0)
        cargo = func.get('cargo', 'Sem cargo')
        
        # USA AS FUNÇÕES DO RH.PY para calcular salários
        # 1. Calcula salário bruto (horas normais × valor/hora)
        salario_bruto = rh.calcular_salario_bruto(horas_normais, valor_hora)
        
        # 2. Calcula valor das horas extras (gerentes/diretores não recebem)
        valor_horas_extras = rh.calcular_horas_extras(horas_extras, valor_hora, cargo)
        
        # 3. Salário total bruto (normal + extras)
        salario_total_bruto = salario_bruto + valor_horas_extras
        
        # 4. Calcula IRPF sobre o salário bruto total
        irpf = rh.calcular_irpf(salario_total_bruto)
        
        # 5. Calcula salário líquido (bruto - IRPF)
        salario_liquido = rh.calcular_liquido(salario_total_bruto, irpf)
        
        # Adiciona aos detalhes
        detalhes_funcionarios.append({
            'nome': nome,
            'cargo': cargo,
            'valor_hora': valor_hora,
            'horas_normais': horas_normais,
            'horas_extras': horas_extras,
            'salario_bruto': salario_bruto,
            'valor_horas_extras': valor_horas_extras,
            'salario_total_bruto': salario_total_bruto,
            'irpf': irpf,
            'salario_liquido': salario_liquido
        })
        
        # Soma aos totais
        custo_total_bruto += salario_total_bruto
        custo_total_liquido += salario_liquido
        total_irpf += irpf
    
    return {
        'tipo': 'Salários',
        'qtd_funcionarios': len(funcionarios),
        'horas_normais': horas_normais,
        'horas_extras': horas_extras,
        'custo_total_bruto': custo_total_bruto,
        'custo_total_liquido': custo_total_liquido,
        'total_irpf': total_irpf,
        'detalhes': detalhes_funcionarios
    }


def gerar_relatorio_fabrica(dias_trabalhados=30):
    """
    Gera um relatório completo e formatado dos custos de água e energia.
    
    Mostra:
    - Informações gerais (funcionários, dias, horas)
    - Detalhamento do custo de água
    - Detalhamento do custo de energia (gerador + rede)
    - Resumo total mensal
    """
    # Imprime o cabeçalho do relatório
    print("\n" + "="*80)
    print("RELATÓRIO DE CUSTOS DE UTILIDADES - FÁBRICA 24/7".center(80))
    print("="*80)
    
    # Carrega os funcionários cadastrados
    funcionarios = data_manager.load_data('funcionarios.json')
    
    # Se não há funcionários, exibe aviso e sai
    if not funcionarios:
        print("\n⚠ ATENÇÃO: Nenhum funcionário cadastrado!")
        print("Cadastre funcionários no módulo RH primeiro.")
        print("="*80)
        return None
    
    # Calcula os custos de água, energia e salários
    agua = calcular_custo_agua_fabrica(dias_trabalhados)
    energia = calcular_custo_luz_fabrica(dias_trabalhados)
    salarios = calcular_salarios_fabrica()

    # ========== SEÇÃO 1: INFORMAÇÕES GERAIS ==========
    print(f"\n📊 INFORMAÇÕES GERAIS")
    print("-"*80)
    print(f"Funcionários: {agua['qtd_funcionarios']}")  # Quantidade de funcionários
    print(f"Dias/mês: {dias_trabalhados}")              # Dias trabalhados no mês
    print(f"Operação: 24h/dia")                         # Fábrica funciona 24h
    print(f"Total horas/mês: {agua['total_horas']}h")   # Total de horas (24 × 30 = 720)
    
    # ========== SEÇÃO 2: CUSTO DE ÁGUA ==========
    print(f"\n💧 ÁGUA")
    print("-"*80)
    # Mostra a fórmula do cálculo
    print(f"R$ {agua['custo_por_hora']:.2f}/h × {agua['total_horas']}h × {agua['qtd_funcionarios']} funcionários")
    # Mostra o resultado
    print(f"💰 Total: R$ {agua['custo_total']:.2f}")
    
    # ========== SEÇÃO 3: CUSTO DE ENERGIA ==========
    print(f"\n⚡ ENERGIA")
    print("-"*80)
    
    # Custo do gerador (8 horas por dia)
    print(f"🔋 Gerador (8h/dia): {8 * dias_trabalhados}h × {agua['qtd_funcionarios']} × R$ 1.60 = R$ {energia['custo_gerador']:.2f}")
    
    # Custo da rede elétrica (16 horas por dia)
    print(f"🔌 Rede (16h/dia): {16 * dias_trabalhados}h × {agua['qtd_funcionarios']} × R$ 2.40 = R$ {energia['custo_rede']:.2f}")
    
    # Total de energia (gerador + rede)
    print(f"💰 Total: R$ {energia['custo_total']:.2f}")

    # ========== SEÇÃO 4: SALÁRIOS ==========
    print(f"\n💵 SALÁRIOS")
    print("-"*80)
    print(f"Horas normais: {salarios['horas_normais']}h/mês")
    print(f"Horas extras: {salarios['horas_extras']}h/mês")
    print()
    
    if salarios['qtd_funcionarios'] > 0:
        for detalhe in salarios['detalhes']:
            print(f"👤 {detalhe['nome']} - {detalhe['cargo']}")
            print(f"   Salário Base: R$ {detalhe['salario_bruto']:.2f}")
            print(f"   Extras: R$ {detalhe['valor_horas_extras']:.2f}")
            print(f"   IRPF: -R$ {detalhe['irpf']:.2f}")
            print(f"   💰 Líquido: R$ {detalhe['salario_liquido']:.2f}")
            print()

    print(f"💰 Total Salários (Bruto): R$ {salarios['custo_total_bruto']:.2f}")
    print(f"💰 Total Salários (Líquido): R$ {salarios['custo_total_liquido']:.2f}")
    
    # ========== SEÇÃO 5: RESUMO TOTAL ==========
    total = agua['custo_total'] + energia['custo_total'] + salarios['custo_total_bruto']  # Soma água + energia + salários brutos (custo empresa)
    print("\n" + "="*80)
    print("📊 RESUMO MENSAL")
    print("="*80)
    print(f"Água:             R$ {agua['custo_total']:>12.2f}")      # Custo de água
    print(f"Energia:          R$ {energia['custo_total']:>12.2f}")   # Custo de energia
    print(f"Salários (Bruto): R$ {salarios['custo_total_bruto']:>12.2f}") # Custo salários
    print("-"*80)
    print(f"TOTAL:            R$ {total:>12.2f}")                    # Custo total
    print("="*80)
    
    # Retorna os dados calculados para uso posterior se necessário
    return {'agua': agua, 'energia': energia, 'salarios': salarios, 'total': total}


# ============================================================================
# FUNÇÕES PARA COMPATIBILIDADE COM MAIN.PY
# ============================================================================
# Estas funções são usadas pelo menu principal (main.py) para outras operações

def cadastrar_despesas_fixas():
    """
    Permite cadastrar despesas fixas manualmente (água, luz, salários, impostos).
    
    Esta função pede ao usuário para digitar os valores e salva em um arquivo JSON.
    É diferente da função automática da fábrica - aqui você digita os valores.
    """
    print("\n--- Cadastro de Despesas Fixas ---")
    try:
        # Pede ao usuário para digitar cada despesa
        agua = float(input("Água: R$ "))
        luz = float(input("Luz: R$ "))
        salarios = float(input("Salários: R$ "))
        impostos = float(input("Impostos: R$ "))
        
        # Cria uma lista com todas as despesas
        despesas = [
            {"tipo": "Agua", "valor": agua},
            {"tipo": "Luz", "valor": luz},
            {"tipo": "Salarios", "valor": salarios},
            {"tipo": "Impostos", "valor": impostos}
        ]
        
        # Salva as despesas no arquivo despesas.json
        data_manager.save_data('despesas.json', despesas)
        
        # Calcula e mostra o total
        total = agua + luz + salarios + impostos
        print(f"\n✓ Despesas cadastradas! Total: R$ {total:.2f}")
        return total
        
    except ValueError:
        # Se o usuário digitar algo que não é número, mostra erro
        print("Erro: Digite apenas valores numéricos.")
        return 0.0

def calcular_custo_producao(despesas_fixas, custo_insumos):
    """
    Calcula o custo total de produção.
    
    Fórmula simples: Despesas Fixas + Custo dos Insumos = Custo Total
    Exemplo: R$ 10.000 + R$ 5.000 = R$ 15.000
    """
    return despesas_fixas + custo_insumos

def calcular_custo_por_carro(custo_total, qtd_carros):
    """
    Calcula quanto custa produzir cada carro.
    
    Fórmula: Custo Total ÷ Quantidade de Carros = Custo por Carro
    Exemplo: R$ 15.000 ÷ 10 carros = R$ 1.500 por carro
    """
    # Se não produziu nenhum carro, retorna 0 para evitar divisão por zero
    return custo_total / qtd_carros if qtd_carros > 0 else 0.0

def calcular_preco_venda(custo_unitario):
    """
    Calcula o preço de venda com 50% de lucro.
    
    Fórmula: Custo × 1.5 = Preço de Venda (50% de lucro)
    Exemplo: R$ 1.500 × 1.5 = R$ 2.250
    """
    return custo_unitario * 1.5


# ============================================================================
# TESTE DO MÓDULO
# ============================================================================
# Este código só executa quando você roda: python modules/financeiro.py

if __name__ == "__main__":
    print("Módulo Financeiro - Teste")
    
    # Carrega os funcionários cadastrados
    funcionarios = data_manager.load_data('funcionarios.json')
    
    # Verifica se há funcionários
    if not funcionarios:
        print("\n⚠ Nenhum funcionário cadastrado.")
        print("Execute: python modules/rh.py")
    else:
        # Se há funcionários, mostra quantos e gera o relatório
        print(f"\n✓ {len(funcionarios)} funcionário(s) encontrado(s)")
        print("\nGerando relatório da fábrica (30 dias)...")
        gerar_relatorio_fabrica()
