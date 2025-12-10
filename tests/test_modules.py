import sys
import os
import unittest
from unittest.mock import patch, mock_open, MagicMock

# Adiciona o diretório atual ao path para importar os módulos
sys.path.append(os.getcwd())

from modules import operacional, estoque, financeiro, rh, data_manager

class TestModules(unittest.TestCase):

    # =======================================================================
    # TESTES: DATA_MANAGER
    # =======================================================================
    def test_data_manager_load_save(self):
        print("\n[TEST] Data Manager")
        filename = "test_data.json"
        data = [{"id": 1, "name": "Test"}]
        
        # Test Save
        with patch("builtins.open", mock_open()) as mock_file:
            success = data_manager.save_data(filename, data)
            self.assertTrue(success, "Falha ao salvar dados")
            mock_file.assert_called_with(os.path.join(data_manager.DATA_DIR, filename), 'w', encoding='utf-8')

        # Test Load (Success)
        with patch("builtins.open", mock_open(read_data='[{"id": 1, "name": "Test"}]')) as mock_file:
            with patch("os.path.exists", return_value=True):
                loaded_data = data_manager.load_data(filename)
                self.assertEqual(loaded_data, data, "Dados carregados incorretos")

        # Test Load (File Not Found)
        with patch("os.path.exists", return_value=False):
            loaded_data = data_manager.load_data("non_existent.json")
            self.assertEqual(loaded_data, [], "Deve retornar lista vazia se arquivo não existe")
        print("  - Save/Load: OK")

    # =======================================================================
    # TESTES: ESTOQUE
    # =======================================================================
    def test_estoque(self):
        print("\n[TEST] Estoque")
        # Reset global stock for test
        estoque.estoque = []
        
        # Manually add a product to simulate state
        produto_teste = {
            "codigo": "001",
            "nome": "Item A",
            "quantidade": 10,
            "valor_unitario": 100.0,
            "local": "A1"
        }
        estoque.estoque.append(produto_teste)
        
        # Test produto_existe
        existente = estoque.produto_existe("001", "Item B") # Search by code
        self.assertEqual(existente, produto_teste, "Falha ao encontrar produto por código")
        
        existente = estoque.produto_existe("999", "Item A") # Search by name
        self.assertEqual(existente, produto_teste, "Falha ao encontrar produto por nome")
        
        inexistente = estoque.produto_existe("999", "Item Z")
        self.assertIsNone(inexistente, "Falso positivo em produto inexistente")
        print("  - Verificação de existência: OK")

        # Note: entrada_produtos and saida_produtos are highly interactive (lots of input()), 
        # so we rely on verifying the logic helper functions and state manipulation works.

    # =======================================================================
    # TESTES: FINANCEIRO
    # =======================================================================
    def test_financeiro(self):
        print("\n[TEST] Financeiro")
        
        # 1. Custo Produção / Por Carro / Preço Venda
        custo_prod = financeiro.calcular_custo_producao(1000, 500)
        self.assertEqual(custo_prod, 1500, "Custo produção incorreto")
        
        custo_unit = financeiro.calcular_custo_por_carro(1500, 10)
        self.assertEqual(custo_unit, 150.0, "Custo unitário incorreto")
        
        preco = financeiro.calcular_preco_venda(100.0)
        self.assertEqual(preco, 150.0, "Preço venda incorreto (esperado 50% lucro)")
        print("  - Cálculos básicos: OK")

        # 2. Custos de Fábrica (Mocking data_manager to avoid file dependency)
        mock_funcionarios = [
            {"nome": "Func1", "cargo": "Operario", "valor_hora": 10.0},
            {"nome": "Func2", "cargo": "Gerente", "valor_hora": 50.0}
        ]
        
        with patch("modules.data_manager.load_data", return_value=mock_funcionarios):
            # Test Water Cost (2 employees * 1.50 * 24h * 30days) = 2 * 1.5 * 720 = 2160
            agua = financeiro.calcular_custo_agua_fabrica()
            self.assertEqual(agua['custo_total'], 2160.0, f"Custo água incorreto: {agua['custo_total']}")
            
            # Test Energy Cost
            # Gerador (8h): 8 * 30 * 2 * 1.60 = 240 * 2 * 1.60 = 768
            # Rede (16h): 16 * 30 * 2 * 2.40 = 480 * 2 * 2.40 = 2304
            # Total = 3072
            energia = financeiro.calcular_custo_luz_fabrica()
            self.assertAlmostEqual(energia['custo_total'], 3072.0, msg=f"Custo energia incorreto: {energia['custo_total']}")
        print("  - Custos Fábrica (Água/Luz): OK")

    # =======================================================================
    # TESTES: RH
    # =======================================================================
    def test_rh(self):
        print("\n[TEST] RH")
        
        # Test Salário Bruto
        bruto = rh.calcular_salario_bruto(220, 10.0)
        self.assertEqual(bruto, 2200.0, "Cálculo salário bruto incorreto")

        # Test Hora Extra
        extra_op = rh.calcular_horas_extras(10, 10.0, "Operario")
        self.assertEqual(extra_op, 150.0, "Hora extra operário incorreta") # 10 * 15.0
        
        extra_ger = rh.calcular_horas_extras(10, 50.0, "Gerente")
        self.assertEqual(extra_ger, 0.0, "Gerente não deve receber hora extra")
        
        # Test IRPF
        self.assertEqual(rh.calcular_irpf(2000.0), 0.0, "Erro faixa isenta IRPF")
        # 2500 * 0.075 - 169.44 = 187.5 - 169.44 = 18.06
        self.assertAlmostEqual(rh.calcular_irpf(2500.0), 18.06, places=2, msg="Erro faixa 2 IRPF")

        # Test Líquido
        # Bruto 3000 -> IRPF (3000 * 0.15 - 381.44) = 450 - 381.44 = 68.56
        # Liquido = 3000 - 68.56 = 2931.44
        irpf_3k = rh.calcular_irpf(3000.0)
        liquido = rh.calcular_liquido(3000.0, irpf_3k)
        self.assertAlmostEqual(liquido, 3000.0 - 68.56, places=2, msg="Cálculo líquido incorreto")
        
        # Test Matrícula
        # 1. Mock obter_proximo_sequencial to return predictable value
        with patch("modules.rh.obter_proximo_sequencial", return_value=1):
            # Mock random to return fixed digit
            with patch("modules.rh.random.randint", return_value=7):
                # Operacional (1), Auxiliar de Produção (1) -> Expect 110017
                matricula = rh.gerar_matricula("OPERACIONAL", "Auxiliar de Produção", [])
                self.assertEqual(matricula, "110017", f"Matrícula gerada incorretamente: {matricula}")
        print("  - Cálculos RH e Matrícula: OK")

    # =======================================================================
    # TESTES: OPERACIONAL
    # =======================================================================
    def test_operacional(self):
        print("\n[TEST] Operacional")
        
        # Test Estatísticas
        dados = [
            {"dia": "Segunda", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}}, # 250
            {"dia": "Terça", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},   # 250
            {"dia": "Quarta", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},  # 250
            {"dia": "Quinta", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},  # 250
            {"dia": "Sexta", "turnos": {"Manhã": 100, "Tarde": 100, "Noite": 50}},   # 250
            {"dia": "Sábado", "turnos": {"Manhã": 50, "Tarde": 50, "Noite": 0}},     # 100
            {"dia": "Domingo", "turnos": {"Manhã": 0, "Tarde": 0, "Noite": 0}},      # 0
        ] # Total = 1350
        
        stats = operacional.calcular_estatisticas(dados)
        self.assertEqual(stats['total_semanal'], 1350, "Total semanal incorreto")
        self.assertAlmostEqual(stats['media_diaria'], 1350/7, places=2, msg="Média diária incorreta")
        
        # Test Simulação
        mensal, anual = operacional.simular_producao(1350)
        self.assertEqual(mensal, 1350 * 4, "Simulação mensal incorreta")
        self.assertEqual(anual, 1350 * 52, "Simulação anual incorreta")
        
        # Test Capacidade Ideal (User input handled via args)
        ideal = operacional.calcular_capacidade_ideal(meta_mensal=1000)
        self.assertEqual(ideal['mensal'], 1000)
        self.assertEqual(ideal['semanal'], 250)
        self.assertEqual(ideal['anual'], 12000)
        print("  - Estatísticas e Metas: OK")

if __name__ == "__main__":
    unittest.main()
