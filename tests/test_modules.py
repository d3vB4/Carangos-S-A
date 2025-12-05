import sys
import os

# Adiciona o diretório atual ao path para importar os módulos
sys.path.append(os.getcwd())

from modules import operacional, estoque, financeiro, rh

def test_operacional():
    print("\n[TEST] Operacional")
    # Mock dados
    dados = [
        {"dia": "Segunda", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
        {"dia": "Terça", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
        {"dia": "Quarta", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
        {"dia": "Quinta", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
        {"dia": "Sexta", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
        {"dia": "Sábado", "turnos": {"Manhã": 50, "Tarde": 50, "Noite": 0}},
        {"dia": "Domingo", "turnos": {"Manhã": 0, "Tarde": 0, "Noite": 0}},
    ]
    
    stats = operacional.calcular_estatisticas(dados)
    assert stats['total_semanal'] == 1350, f"Total semanal incorreto: {stats['total_semanal']}"
    print("  - Cálculo estatísticas: OK")
    
    mensal, anual = operacional.simular_producao(stats['total_semanal'])
    assert mensal == 1350 * 4, "Simulação mensal incorreta"
    print("  - Simulação: OK")

def test_estoque():
    print("\n[TEST] Estoque")
    estoque.produtos = [] # Reset
    estoque.cadastrar_produto(1, "Item A", "01/01/2024", "Forn A", 10, 100.0)
    
    # Teste duplicidade
    assert estoque.verificar_duplicidade(1) == True, "Falha na verificação de duplicidade"
    assert estoque.verificar_duplicidade(2) == False, "Falso positivo em duplicidade"
    print("  - Duplicidade: OK")
    
    # Teste pesquisa
    res = estoque.pesquisar_produto("Item A")
    assert len(res) == 1, "Falha na pesquisa"
    print("  - Pesquisa: OK")
    
    # Teste custos
    custos = estoque.calcular_custos()
    assert custos['total_atual'] == 1000.0, f"Custo total incorreto: {custos['total_atual']}"
    print("  - Custos: OK")

def test_financeiro():
    print("\n[TEST] Financeiro")
    custo_prod = financeiro.calcular_custo_producao(1000, 500)
    assert custo_prod == 1500, "Custo produção incorreto"
    
    custo_unit = financeiro.calcular_custo_por_carro(1500, 10)
    assert custo_unit == 150.0, "Custo unitário incorreto"
    
    preco = financeiro.calcular_preco_venda(100.0)
    assert preco == 150.0, "Preço venda incorreto (esperado 50% lucro)"
    print("  - Cálculos financeiros: OK")

def test_rh():
    print("\n[TEST] RH")
    # Teste hora extra
    extra_op = rh.calcular_horas_extras(10, 10.0, "Operario")
    assert extra_op == 150.0, f"Hora extra operário incorreta: {extra_op}" # 10 * (10 * 1.5) = 150
    
    extra_ger = rh.calcular_horas_extras(10, 50.0, "Gerente")
    assert extra_ger == 0.0, "Gerente não deve receber hora extra"
    print("  - Hora extra: OK")
    
    # Teste IRPF (Faixa 1 - Isento)
    irpf_isento = rh.calcular_irpf(2000.0)
    assert irpf_isento == 0.0, "Erro faixa isenta IRPF"
    
    # Teste IRPF (Faixa 2)
    # 2500 * 0.075 - 169.44 = 187.5 - 169.44 = 18.06
    irpf_faixa2 = rh.calcular_irpf(2500.0)
    assert abs(irpf_faixa2 - 18.06) < 0.1, f"Erro faixa 2 IRPF: {irpf_faixa2}"
    print("  - IRPF: OK")

if __name__ == "__main__":
    try:
        test_operacional()
        test_estoque()
        test_financeiro()
        test_rh()
        print("\n[SUCESSO] Todos os testes passaram!")
    except AssertionError as e:
        print(f"\n[FALHA] {e}")
    except Exception as e:
        print(f"\n[ERRO] {e}")
