import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

import main
from modules import data_manager

class TestTerminalFlow(unittest.TestCase):

    @patch('modules.data_manager.load_data')
    @patch('getpass.getpass')
    @patch('builtins.input')
    def test_login_success(self, mock_input, mock_getpass, mock_load_data):
        """Test successful login flow"""
        # Mock Data
        mock_load_data.return_value = [
            {'username': 'admin', 'password': 'scrypt:32768:8:1$mockhash$mockhash', 'role': 'admin'}
        ]
        
        # Mock Inputs: Username
        mock_input.side_effect = ['admin']
        # Mock Password
        mock_getpass.return_value = 'admin123'
        
        # Mock check_password_hash to return True
        with patch('main.check_password_hash', return_value=True):
            user = main.login()
            
        self.assertIsNotNone(user)
        self.assertEqual(user['username'], 'admin')

    @patch('modules.data_manager.load_data')
    @patch('getpass.getpass')
    @patch('builtins.input')
    @patch('sys.exit')
    def test_login_failure_exit(self, mock_exit, mock_input, mock_getpass, mock_load_data):
        """Test login failure and exit"""
        mock_load_data.return_value = [] # No users
        
        # Inputs: Username, Retry? (N)
        mock_input.side_effect = ['wronguser', 'N'] 
        mock_getpass.return_value = 'wrongpass'
        
        # Ensure we don't get stuck in loop if N doesn't work
        with patch('sys.exit') as mock_exit_call:
             mock_exit_call.side_effect = SystemExit # Raise SystemExit to break loop
             with self.assertRaises(SystemExit):
                 main.login()

    @patch('modules.operacional.cadastrar_producao')
    @patch('builtins.input')
    def test_menu_operacional_cadastro(self, mock_input, mock_cadastrar):
        """Test navigating to Operacional -> Cadastrar Produção"""
        # Inputs: Option 1 (Cadastrar), Pause (Enter), Option 0 (Voltar)
        mock_input.side_effect = ['1', '', '0']
        
        main.menu_operacional()
        
        mock_cadastrar.assert_called_once()

    @patch('modules.estoque.cadastrar_produto')
    @patch('builtins.input')
    def test_menu_estoque_cadastro(self, mock_input, mock_cadastrar):
        """Test navigating to Estoque -> Cadastrar Produto with inputs"""
        # Inputs: 
        # 1 (Cadastrar)
        # Código, Nome, Data, Fornecedor, Qtd, Valor
        # Pause (Enter)
        # 0 (Voltar)
        mock_input.side_effect = [
            '1', 
            '99', 'Produto Teste', '01/01/2024', 'Forn Teste', '10', '100.0',
            '', 
            '0'
        ]
        
        main.menu_estoque()
        
        mock_cadastrar.assert_called_once_with(99, 'Produto Teste', '01/01/2024', 'Forn Teste', 10, 100.0)

    @patch('modules.rh.cadastrar_funcionario')
    @patch('builtins.input')
    def test_menu_rh_cadastro(self, mock_input, mock_cadastrar):
        """Test navigating to RH -> Cadastrar Funcionário with inputs"""
        # Inputs:
        # 1 (Cadastrar)
        # Nome, CPF, RG, Endereco, Telefone, Filhos, Cargo, ValorHora
        # Pause (Enter)
        # 0 (Voltar)
        mock_input.side_effect = [
            '1',
            'Func Teste', '123456', 'RG123', 'Rua Teste', '9999-9999', '2', 'Operario', '50.0',
            '',
            '0'
        ]
        
        main.menu_rh()
        
        mock_cadastrar.assert_called_once_with('Func Teste', '123456', 'RG123', 'Rua Teste', '9999-9999', 2, 'Operario', 50.0)

    @patch('modules.financeiro.cadastrar_despesas_fixas')
    @patch('builtins.input')
    def test_menu_financeiro_cadastro(self, mock_input, mock_cadastrar):
        """Test navigating to Financeiro -> Cadastrar Despesas"""
        # Inputs: 1 (Cadastrar), Pause, 0 (Voltar)
        mock_input.side_effect = ['1', '', '0']
        
        main.menu_financeiro()
        
        mock_cadastrar.assert_called_once()

    @patch('modules.data_manager.load_data')
    @patch('modules.operacional.gerar_relatorio')
    @patch('builtins.input')
    def test_menu_operacional_relatorio(self, mock_input, mock_gerar_relatorio, mock_load_data):
        """Test navigating to Operacional -> Ver Relatório"""
        # Mock Data
        mock_load_data.return_value = [
            {'dia': 'Segunda', 'turno': 'Manhã', 'quantidade': 10}
        ]
        
        # Inputs: 2 (Relatório), Pause, 0 (Voltar)
        mock_input.side_effect = ['2', '', '0']
        
        main.menu_operacional()
        
        mock_gerar_relatorio.assert_called_once()

    @patch('modules.estoque.pesquisar_produto')
    @patch('builtins.input')
    def test_menu_estoque_busca(self, mock_input, mock_pesquisar):
        """Test navigating to Estoque -> Buscar Produto"""
        mock_pesquisar.return_value = [{'codigo': 1, 'nome': 'Test', 'quantidade': 10, 'valor_compra': 100}]
        
        # Inputs: 2 (Buscar), Termo, Pause, 0 (Voltar)
        mock_input.side_effect = ['2', 'Test', '', '0']
        
        main.menu_estoque()
        
        mock_pesquisar.assert_called_once_with('Test')

    @patch('modules.data_manager.load_data')
    @patch('modules.estoque.calcular_custos')
    @patch('builtins.input')
    def test_menu_estoque_custos(self, mock_input, mock_calcular, mock_load_data):
        """Test navigating to Estoque -> Relatório Custos"""
        mock_load_data.return_value = []
        mock_calcular.return_value = {'total_atual': 0, 'mensal_projetado': 0, 'anual_projetado': 0}
        
        # Inputs: 3 (Custos), Pause, 0 (Voltar)
        mock_input.side_effect = ['3', '', '0']
        
        main.menu_estoque()
        
        mock_calcular.assert_called_once()

    @patch('modules.data_manager.load_data')
    @patch('modules.financeiro.calcular_preco_venda')
    @patch('builtins.input')
    def test_menu_financeiro_relatorio(self, mock_input, mock_calc_preco, mock_load_data):
        """Test navigating to Financeiro -> Relatório"""
        # Mock Data for despesas, produtos, producao calls
        mock_load_data.side_effect = [
            [{'valor': 100}], # Despesas
            [{'quantidade': 10, 'valor_compra': 10}], # Produtos
            [{'quantidade': 5}] # Producao
        ]
        mock_calc_preco.return_value = 100.0
        
        # Inputs: 2 (Relatório), Pause, 0 (Voltar)
        mock_input.side_effect = ['2', '', '0']
        
        main.menu_financeiro()
        
        mock_calc_preco.assert_called_once()

    @patch('modules.rh.gerar_folha_pagamento')
    @patch('builtins.input')
    def test_menu_rh_folha(self, mock_input, mock_gerar_folha):
        """Test navigating to RH -> Folha de Pagamento"""
        # Inputs: 2 (Folha), Pause, 0 (Voltar)
        mock_input.side_effect = ['2', '', '0']
        
        main.menu_rh()
        
        mock_gerar_folha.assert_called_once()

    @patch('modules.rh.cadastrar_funcionario')
    @patch('modules.operacional.cadastrar_producao')
    @patch('modules.estoque.cadastrar_produto')
    @patch('modules.data_manager.load_data')
    @patch('getpass.getpass')
    @patch('builtins.input')
    @patch('sys.exit')
    def test_full_workflow(self, mock_exit, mock_input, mock_getpass, mock_load_data, mock_estoque_cad, mock_operacional_cad, mock_rh_cad):
        """Test a full end-to-end user session"""
        
        # Mock Data for Login
        mock_load_data.return_value = [
            {'username': 'admin', 'password': 'scrypt:32768:8:1$mockhash$mockhash', 'role': 'admin'}
        ]
        
        # Mock Inputs Sequence:
        # 1. Login: 'admin'
        # 2. Menu Principal -> Estoque: '2'
        # 3. Estoque -> Cadastrar: '1'
        # 4. Estoque Inputs: 999, 'Turbo Compressor', '01/01/2025', 'Garrett', 5, 2500.0
        # 5. Pause: ''
        # 6. Estoque -> Voltar: '0'
        # 7. Menu Principal -> Operacional: '1'
        # 8. Operacional -> Registrar: '1'
        # 9. Operacional Inputs: 'Sexta', 'Noite', 50
        # 10. Pause: ''
        # 11. Operacional -> Voltar: '0'
        # 12. Menu Principal -> RH: '4'
        # 13. RH -> Cadastrar: '1'
        # 14. RH Inputs: 'Maria Engenheira', '123.456.789-00', 'RG-999', 'Av. Brasil', '11 99999-9999', 1, 'Engenheira', 120.0
        # 15. Pause: ''
        # 16. RH -> Voltar: '0'
        # 17. Menu Principal -> Sair: '0'
        
        mock_input.side_effect = [
            'admin', # Login User
            '2', # Menu Principal -> Estoque
            '1', # Estoque -> Cadastrar
            '999', 'Turbo Compressor', '01/01/2025', 'Garrett', '5', '2500.0', # Estoque Inputs
            '', # Pause
            '0', # Estoque -> Voltar
            '1', # Menu Principal -> Operacional
            '1', # Operacional -> Registrar
            # Note: operacional.cadastrar_producao in main.py calls the module function directly which has its own inputs.
            # Wait, main.py calls operacional.cadastrar_producao() which does inputs internally?
            # Let's check main.py again. 
            # main.py:
            # if opcao == '1':
            #    operacional.cadastrar_producao()
            # So main.py DOES NOT collect inputs for operacional, it calls the function.
            # But wait, I am mocking operacional.cadastrar_producao.
            # If I mock it, it won't ask for inputs!
            # So I don't need to provide inputs for operacional.cadastrar_producao here if I mock it.
            # BUT, for Estoque and RH, main.py collects inputs THEN calls the function.
            # So for Estoque and RH I MUST provide inputs.
            # For Operacional, main.py calls the function directly.
            # So the inputs for Operacional are NOT needed in main.py's input stream if I mock the function.
            
            # Corrected Sequence:
            # ...
            # 7. Menu Principal -> Operacional: '1'
            # 8. Operacional -> Registrar: '1'
            # (Mocked function called here, no inputs needed from main.py perspective)
            # 9. Pause: ''
            # 10. Operacional -> Voltar: '0'
            # ...
            
            '', # Pause (after operational)
            '0', # Operacional -> Voltar
            '4', # Menu Principal -> RH
            '1', # RH -> Cadastrar
            'Maria Engenheira', '123.456.789-00', 'RG-999', 'Av. Brasil', '11 99999-9999', '1', 'Engenheira', '120.0', # RH Inputs
            '', # Pause
            '0', # RH -> Voltar
            '0' # Menu Principal -> Sair
        ]
        
        mock_getpass.return_value = 'admin123'
        
        # Mock check_password_hash
        with patch('main.check_password_hash', return_value=True):
            # Run the full flow
            # We need to catch SystemExit because option '0' calls sys.exit()
            mock_exit.side_effect = SystemExit
            with self.assertRaises(SystemExit):
                user = main.login()
                main.menu_principal(user)
        
        # Verifications
        
        # 1. Verify Estoque Registration
        mock_estoque_cad.assert_called_once_with(999, 'Turbo Compressor', '01/01/2025', 'Garrett', 5, 2500.0)
        
        # 2. Verify Operacional Registration
        mock_operacional_cad.assert_called_once()
        
        # 3. Verify RH Registration
        mock_rh_cad.assert_called_once_with('Maria Engenheira', '123.456.789-00', 'RG-999', 'Av. Brasil', '11 99999-9999', 1, 'Engenheira', 120.0)

if __name__ == '__main__':
    unittest.main()
