import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import json

# Adiciona o diretório raiz ao path
sys.path.append(os.getcwd())

from modules import operacional

class TestOperacional(unittest.TestCase):
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.dados_exemplo = [
            {"dia": "Segunda", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
            {"dia": "Terça", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
            {"dia": "Quarta", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
            {"dia": "Quinta", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
            {"dia": "Sexta", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},
            {"dia": "Sábado", "turnos": {"Manhã": 50, "Tarde": 50, "Noite": 0}},
            {"dia": "Domingo", "turnos": {"Manhã": 0, "Tarde": 0, "Noite": 0}},
        ]
        
    def test_calcular_estatisticas(self):
        """Testa o cálculo de estatísticas (totais e médias)"""
        stats = operacional.calcular_estatisticas(self.dados_exemplo)
        
        # 5 dias * 250 + 1 dia * 100 = 1250 + 100 = 1350
        self.assertEqual(stats['total_semanal'], 1350)
        self.assertAlmostEqual(stats['media_diaria'], 1350 / 7, places=2)
        
        # Testar média por turno
        # Manhã: (5*100 + 50) / 7 = 550 / 7 = 78.57
        # Tarde: (5*100 + 50) / 7 = 550 / 7 = 78.57
        # Noite: (5*50) / 7 = 250 / 7 = 35.71
        self.assertAlmostEqual(stats['media_por_turno']['Manhã'], 550/7, places=2)
        self.assertAlmostEqual(stats['media_por_turno']['Noite'], 250/7, places=2)

    def test_simular_producao(self):
        """Testa a projeção mensal e anual"""
        total_semanal = 1000
        mensal, anual = operacional.simular_producao(total_semanal)
        
        self.assertEqual(mensal, 4000) # 1000 * 4
        self.assertEqual(anual, 52000) # 1000 * 52

    @patch('builtins.input', return_value='1000') # Simula entrada do usuário de 1000 como meta mensal
    @patch('builtins.print')
    def test_calcular_capacidade_ideal_input(self, mock_print, mock_input):
        """Testa o cálculo da capacidade ideal com input do usuário"""
        # Teste sem argumento (ativa input)
        ideal = operacional.calcular_capacidade_ideal()
        
        self.assertEqual(ideal['mensal'], 1000)
        self.assertEqual(ideal['semanal'], 250) # 1000 / 4
        self.assertEqual(ideal['anual'], 12000) # 1000 * 12
        
    def test_calcular_capacidade_ideal_argumento(self):
        """Testa o cálculo da capacidade ideal passando argumento direto"""
        ideal = operacional.calcular_capacidade_ideal(meta_mensal=2000)
        
        self.assertEqual(ideal['mensal'], 2000)
        self.assertEqual(ideal['semanal'], 500)
        self.assertEqual(ideal['anual'], 24000)

    @patch('builtins.input', side_effect=['10', '20', '30'] * 7) # Input para 7 dias * 3 turnos
    @patch('builtins.print') # Silencia prints
    @patch('json.dump') # Mock salvar arquivo
    @patch('os.path.exists', return_value=False) # Finge que arquivo não existe
    def test_cadastrar_producao_sucesso(self, mock_exists, mock_json_dump, mock_print, mock_input):
        """Testa o cadastro de produção com inputs válidos"""
        resultado = operacional.cadastrar_producao()
        
        self.assertEqual(len(resultado), 7)
        self.assertEqual(resultado[0]['dia'], 'Segunda')
        self.assertEqual(resultado[0]['turnos']['Manhã'], 10)
        self.assertEqual(resultado[0]['turnos']['Tarde'], 20)
        self.assertEqual(resultado[0]['turnos']['Noite'], 30)

    @patch('builtins.input', side_effect=['-10', '10', '20', '30'] + ['10', '10', '10'] * 20) # Um erro depois sucesso
    @patch('builtins.print')
    @patch('json.dump')
    @patch('os.path.exists', return_value=False)
    def test_cadastrar_producao_validacao_negativo(self, mock_exists, mock_json_dump, mock_print, mock_input):
        """Testa se o sistema rejeita números negativos"""
        # O side_effect tem um -10 primeiro, que deve ser rejeitado, pedindo input novamente (o 10)
        
        resultado = operacional.cadastrar_producao()
        
        # Verifica se chamou print de erro pelo menos uma vez
        chamadas_erro = [call for call in mock_print.mock_calls if "não pode ser negativa" in str(call)]
        self.assertTrue(len(chamadas_erro) > 0, "Deveria ter exibido erro de valor negativo")

if __name__ == '__main__':
    unittest.main()
