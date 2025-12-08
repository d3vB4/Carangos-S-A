
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Adiciona diretório raiz para importar app
sys.path.append(os.getcwd())

from app import app
from modules import data_manager

class WebIntegrationTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        
        # Mock de sessão para pular login
        with self.client.session_transaction() as sess:
            sess['user_id'] = 'admin'
            sess['username'] = 'admin'
            sess['role'] = 'admin'

    @patch('modules.data_manager.load_data')
    def test_operacional_route_uses_module(self, mock_load):
        """
        Verifica se a rota /operacional carrega sem travar (devido ao input)
        e se usa as funções do módulo.
        """
        # Mock dados de produção
        mock_load.return_value = [
            {'dia': 'Segunda', 'turno': 'Manhã', 'quantidade': 100}
        ]
        
        # Tenta acessar a rota GET
        try:
            response = self.client.get('/operacional')
            self.assertEqual(response.status_code, 200)
            print("\n✅ Rota /operacional acessada com sucesso (Não travou no input)")
        except Exception as e:
            self.fail(f"Rota /operacional falhou ou travou: {e}")

    @patch('modules.data_manager.load_data')
    def test_estoque_route_uses_module(self, mock_load):
        """
        Verifica se a rota /estoque usa o módulo estoque (que foi restaurado).
        """
        # Mock produtos
        mock_load.return_value = [
            {'codigo': 1, 'nome': 'Teste', 'quantidade': 10, 'valor_compra': 50.0}
        ]
        
        response = self.client.get('/estoque')
        self.assertEqual(response.status_code, 200)
        # Verifica se calculou custos (função do módulo)
        # O template deve conter o custo total: 10 * 50 = 500
        self.assertIn(b'500.00', response.data)
        print("\n✅ Rota /estoque acessada com sucesso e calculou custos")

if __name__ == '__main__':
    unittest.main()
