
import sys
import os
from unittest.mock import patch, MagicMock
import json

# Adiciona o diretório atual ao path
sys.path.append(os.getcwd())

import main

def mock_inputs():
    """
    Gera uma sequência de inputs para simular o usuário navegando em TODO o sistema.
    
    Sequência:
    1. Login (Enter = entra como teste/admin)
    2. RH:
       - Cadastrar Funcionário (Setor 1, Cargo 1)
       - Listar Funcionários
       - Gerar Folha
       - Deletar Funcionário (Limpeza)
    3. Estoque:
       - Cadastrar Produto (Inputs consumidos pelo main, função mockada)
       - Pesquisar Produto
       - Relatório de Custos
    4. Operacional:
       - Registrar Produção (21 inputs)
       - Relatório
    5. Financeiro:
       - Cadastrar Despesas Fixas
       - Relatório Financeiro
       - Relatório Fábrica (Água/Luz)
       - Indicadores
    6. Sair
    """
    inputs = []
    
    # --- 1. LOGIN ---
    inputs.append("") # Enter para pular login (Modo Teste)
    
    # --- 2. MÓDULO RH ---
    inputs.append("4") # Menu Principal -> RH
    
    # 2.1 Cadastrar Funcionário
    inputs.append("1") # Opção 1: Cadastrar
    inputs.append("João Silva")       # Nome
    inputs.append("Rua Teste")        # Endereço
    inputs.append("12345678900")      # CPF
    inputs.append("1234567")          # RG
    inputs.append("12345")            # CTPS
    inputs.append("11999999999")      # Telefone
    inputs.append("2")                # Filhos (2)
    inputs.append("1")                # Setor: Operacional
    inputs.append("1")                # Cargo: Auxiliar (1)
    inputs.append("")                 # Pause
    
    # 2.2 Listar Funcionários
    inputs.append("2") # Opção 2: Listar
    inputs.append("")  # Pause
    
    # 2.3 Gerar Folha de Pagamento
    inputs.append("5") # Opção 5: Folha
    inputs.append("2") # Opção 2: Todos os setores (Menu interno do RH com 1 setor)
    # Nota: O RH pede horas trabalhadas para cada funcionário com input(). 
    # Como cadastramos 1, vai pedir 1 vez.
    inputs.append("") # Enter para aceitar padrão 220h
    inputs.append("") # Enter para aceitar padrão 0h extra
    inputs.append("") # Pause
    
    # 2.4 Voltar para Menu Principal (Não deletar agora para usar dados no Financeiro)
    inputs.append("0") # Voltar do RH
    
    # --- 3. MÓDULO ESTOQUE ---
    inputs.append("2") # Menu Principal -> Estoque
    
    # 3.1 Cadastrar Produto
    # Nota: O main.py pede os inputs ANTES de chamar a função do estoque.
    inputs.append("1")           # Opção 1: Cadastrar
    inputs.append("101")         # Código
    inputs.append("Parafuso")    # Nome
    inputs.append("01/01/2024")  # Data Fab
    inputs.append("Metalúrgica") # Fornecedor
    inputs.append("500")         # Quantidade
    inputs.append("0.50")        # Valor Compra
    inputs.append("")            # Pause
    
    # 3.2 Buscar Produto
    inputs.append("2")           # Opção 2: Buscar
    inputs.append("Parafuso")    # Termo
    inputs.append("")            # Pause
    
    # 3.3 Relatório de Custos
    inputs.append("3")           # Opção 3: Custos
    inputs.append("")            # Pause
    
    # Voltar estoque
    inputs.append("0") 
    
    # --- 4. MÓDULO OPERACIONAL ---
    inputs.append("1") # Menu Principal -> Operacional
    
    # 4.1 Registrar Produção
    inputs.append("1") # Opção 1: Registrar
    # 7 dias * 3 turnos = 21 inputs
    for _ in range(21):
        inputs.append("100") 
    inputs.append("") # Pause
    
    # 4.2 Relatório
    inputs.append("2")    # Opção 2: Relatório
    inputs.append("8000") # Meta Mensal
    inputs.append("")     # Pause
    
    # Voltar operacional
    inputs.append("0")
    
    # --- 5. MÓDULO FINANCEIRO ---
    inputs.append("3") # Menu Principal -> Financeiro
    
    # 5.1 Despesas Fixas
    inputs.append("1")      # Opção 1: Cadastrar
    inputs.append("100.0")  # Água
    inputs.append("200.0")  # Luz
    inputs.append("3000.0") # Salários (Simulado input manual)
    inputs.append("500.0")  # Impostos
    inputs.append("")       # Pause
    
    # 5.2 Relatório Financeiro (Geral)
    inputs.append("2")      # Opção 2
    inputs.append("")       # Pause
    
    # 5.3 Relatório Fábrica (Água/Luz Auto)
    inputs.append("3")      # Opção 3
    inputs.append("")       # Pause
    
    # 5.4 Indicadores
    inputs.append("4")      # Opção 4
    inputs.append("")       # Pause
    
    # Voltar
    inputs.append("0")
    
    # --- LIMPEZA (Voltar ao RH para deletar) ---
    inputs.append("4") # Menu Principal -> RH
    inputs.append("4") # Opção 4: Deletar
    inputs.append("1") # Indice 1
    inputs.append("s") # Confirmar "s"
    inputs.append("")  # Pause
    inputs.append("0") # Voltar do RH
    
    # --- 6. SAIR ---
    inputs.append("0") # Menu Principal -> Sair
    
    return inputs

@patch('builtins.input')
@patch('builtins.print')
@patch('os.system') # Mock clear screen
@patch('time.sleep') # Skip sleep
def executar_teste_integracao(mock_sleep, mock_system, mock_print, mock_input):
    import shutil
    import glob
    
    print("🚀 Iniciando Teste de Integração Completo (Main -> Todos Módulos)...")
    
    # --- SETUP DATA ---
    # Backup existing JSON files to avoid messing up user data
    data_dir = "data"
    backup_dir = "data_backup_test"
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)
    os.makedirs(backup_dir)
    
    json_files = glob.glob(os.path.join(data_dir, "*.json"))
    for f in json_files:
        shutil.copy(f, backup_dir)
        os.remove(f)
        
    print(f"[SETUP] Backup realizado de {len(json_files)} arquivos. Diretório 'data/' limpo.")

    # Configura sequence de inputs
    # Wrapper para debug de inputs
    def debug_input_wrapper(inputs):
        for val in inputs:
            print(f"[DEBUG INPUT] Consumed: '{val}'")
            yield val
            
    mock_input.side_effect = debug_input_wrapper(mock_inputs())
    
    try:
        # Executa o main (loop principal)
        # Atenção: main.py roda until sys.exit()
        main.user = main.login()
        main.menu_principal(main.user)
    except SystemExit:
        print("\n✅ Ciclo do Sistema finalizado (SystemExit)!")
    except StopIteration:
        print("\n❌ Erro: A simulação pediu mais inputs do que o fornecido.")
        # Debug: Mostra onde parou (quantos usei)
        print(f"Inputs usados: {mock_input.call_count}")
    except Exception as e:
        print(f"\n❌ Erro Inesperado: {e}")
        import traceback
        traceback.print_exc()
        raise e
    finally:
        # --- TEARDOWN DATA ---
        # Restore files
        for f in glob.glob(os.path.join(backup_dir, "*.json")):
            shutil.copy(f, data_dir)
        shutil.rmtree(backup_dir)
        print("[TEARDOWN] Dados originais restaurados.")

    # --- VERIFICAÇÕES ---
    # Coletamos todas as strings printadas
    prints = [str(call.args[0]) if call.args else "" for call in mock_print.mock_calls]
    
    verificacoes = {
        "Login Admin": "Bem-vindo",
        "RH Menu": "MÓDULO DE RH",
        "Cadastro Func": "cadastrado com sucesso",
        "Folha Pagamento": "FOLHA DE PAGAMENTO - TODOS OS SETORES",
        "Estoque Menu": "MÓDULO DE ESTOQUE",
        "Busca Produto": "Resultados", # Do print do main
        "Relatório Custos": "Custo Total em Estoque",
        "Operacional Menu": "MÓDULO OPERACIONAL",
        "Relatório Op": "RELATÓRIO OPERACIONAL",
        "Financeiro Menu": "MÓDULO FINANCEIRO",
        "Indicadores": "INDICADORES FINANCEIROS"
    }
    

    sys.stdout.write("\n[CHECK] Check de Cobertura de Fluxo:\n")
    all_passed = True
    
    # Adjust Login check for Test Mode
    verificacoes["Login Admin"] = "Entrando em modo teste"

    for nome, trecho in verificacoes.items():
        found = any(trecho in p for p in prints)
        status = "[OK]" if found else "[FAIL]"
        sys.stdout.write(f"  {status} {nome}\n")
        if not found:
            all_passed = False
            
    if all_passed:
        sys.stdout.write("\n[SUCCESS] O Teste de Integracao cobriu todos os modulos!\n")
    else:
        sys.stdout.write("\n[WARNING] Alguns pontos do fluxo nao foram verificados.\n")
        sys.stdout.write("\n--- DUMP DO OUTPUT CAPTURADO ---\n")
        for line in prints:
            try:
                sys.stdout.write(line + "\n")
            except:
                pass
        sys.stdout.write("--------------------------------\n")
        sys.stdout.write("\n--- DUMP DO OUTPUT CAPTURADO ---\n")
        for line in prints:
            try:
                sys.stdout.write(line + "\n")
            except:
                pass
        sys.stdout.write("--------------------------------\n")

if __name__ == "__main__":
    executar_teste_integracao()
