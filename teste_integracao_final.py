
import sys
import os
from unittest.mock import patch
import json

# Adiciona o diretório atual ao path
sys.path.append(os.getcwd())

import main

def mock_inputs():
    """
    Gera uma sequência de inputs para simular o usuário navegando no menu.
    Fluxo:
    1. Login (Enter = teste)
    2. Menu Principal -> 1 (Operacional)
    3. Menu Operacional -> 1 (Registrar Produção)
    4. Inputs para 7 dias * 3 turnos (21 valores)
    5. Enter (pause)
    6. Menu Operacional -> 2 (Relatório)
    7. Input Meta Mensal (1000)
    8. Enter (pause)
    9. Menu Operacional -> 0 (Voltar)
    10. Menu Principal -> 3 (Financeiro)
    11. Menu Financeiro -> 2 (Relatório Financeiro)
    12. Enter (pause)
    13. Menu Financeiro -> 0 (Voltar)
    14. Menu Principal -> 0 (Sair)
    """
    inputs = []
    
    # 1. Login
    inputs.append("") # Enter para pular login
    
    # 2. Ir para Operacional
    inputs.append("1") 
    
    # 3. Registrar Produção
    inputs.append("1")
    
    # 4. Dados de produção (21 inputs de '100')
    for _ in range(21):
        inputs.append("100")
        
    # 5. Pause
    inputs.append("")
    
    # 6. Relatório Operacional
    inputs.append("2")
    
    # 7. Meta Mensal (Nova funcionalidade)
    inputs.append("8000") # Meta mensal
    
    # 8. Pause
    inputs.append("")
    
    # 9. Voltar do Operacional
    inputs.append("0")
    
    # 10. Ir para Financeiro
    inputs.append("3")
    
    # 11. Relatório Financeiro
    inputs.append("2")
    
    # 12. Pause
    inputs.append("")
    
    # 13. Voltar do Financeiro
    inputs.append("0")
    
    # 14. Sair
    inputs.append("0")
    
    return inputs

@patch('builtins.input')
@patch('builtins.print')
@patch('os.system') # Mock clear screen
@patch('time.sleep') # Skip sleep
def executar_teste_integracao(mock_sleep, mock_system, mock_print, mock_input):
    print("🚀 Iniciando Teste de Integração Completo...")
    
    # Configura os inputs simulados
    mock_input.side_effect = mock_inputs()
    
    try:
        # Executa o main (vai rodar até o sys.exit)
        main.user = main.login()
        main.menu_principal(main.user)
    except SystemExit:
        print("\n✅ Teste finalizado com sucesso (SystemExit chamado)!")
    except StopIteration:
        print("\n❌ Erro: Faltaram inputs na simulação!")
    except Exception as e:
        print(f"\n❌ Erro durante o teste: {e}")
        raise e

    # Verifica se passou pelos pontos chave
    # Procura strings específicas nos prints chamados
    prints = [str(call) for call in mock_print.mock_calls]
    
    verificacoes = {
        "Login": "Bem-vindo",
        "Menu Op": "MÓDULO OPERACIONAL",
        "Relatório Op": "RELATÓRIO OPERACIONAL",
        "Input Meta": "Configuração de Metas",
        "Relatório Fin": "Relatório Financeiro",
        "Saída": "Saindo do sistema"
    }
    
    print("\n📊 Relatório do Teste:")
    for nome, texto in verificacoes.items():
        found = any(texto in p for p in prints)
        status = "✅" if found else "❌"
        print(f"  {status} {nome}: {'Encontrado' if found else 'Não encontrado'}")

if __name__ == "__main__":
    executar_teste_integracao()
