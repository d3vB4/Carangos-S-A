import unittest
import os
import sys

# Add current directory to path
sys.path.append(os.getcwd())

from app import app, init_db

class CarangosAppTestCase(unittest.TestCase):
    def setUp(self):
        # Clean JSON files in data/
        for filename in ['producao.json', 'produtos.json', 'despesas.json', 'funcionarios.json', 'users.json']:
            filepath = os.path.join('data', filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        init_db()

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_rbac_admin_create_user(self):
        # Admin login
        self.login('admin', 'admin123')
        
        # Create RH user
        rv = self.app.post('/users/create', data=dict(
            username='rh_user',
            password='password',
            role='rh'
        ), follow_redirects=True)
        self.assertIn('Usuário rh_user criado com sucesso', rv.data.decode('utf-8'))
        
        # Create Operacional user
        rv = self.app.post('/users/create', data=dict(
            username='op_user',
            password='password',
            role='operacional'
        ), follow_redirects=True)
        self.assertIn('Usuário op_user criado com sucesso', rv.data.decode('utf-8'))

    def test_rbac_module_access(self):
        # Setup users
        self.login('admin', 'admin123')
        # Create users with NEW roles
        self.app.post('/users/create', data=dict(username='func_rh_test', password='password', role='func_rh'))
        self.app.post('/users/create', data=dict(username='func_op_test', password='password', role='func_producao'))
        
        # Test RH Access
        self.login('func_rh_test', 'password')
        rv = self.app.get('/rh')
        self.assertEqual(rv.status_code, 200)
        
        # RH should NOT access Operacional
        rv = self.app.get('/operacional', follow_redirects=True)
        self.assertIn('Acesso negado', rv.data.decode('utf-8'))
        
        # Test Operacional Access
        self.login('func_op_test', 'password')
        rv = self.app.get('/operacional')
        self.assertEqual(rv.status_code, 200)
        
        # Operacional should NOT access RH
        rv = self.app.get('/rh', follow_redirects=True)
        self.assertIn('Acesso negado', rv.data.decode('utf-8'))

    def test_module_integration(self):
        # Setup admin
        self.login('admin', 'admin123')
        
        # 1. Operacional: Register Production
        rv = self.app.post('/operacional', data=dict(
            dia='Segunda',
            turno='Manhã',
            quantidade=100
        ), follow_redirects=True)
        self.assertIn('Produção registrada com sucesso', rv.data.decode('utf-8'))
        
        # 2. Estoque: Register Product
        rv = self.app.post('/estoque', data=dict(
            codigo='P001',
            nome='Roda',
            data_fabricacao='2023-01-01',
            fornecedor='Forn A',
            quantidade=50,
            valor_compra=100.00
        ), follow_redirects=True)
        self.assertIn('Produto Roda cadastrado com sucesso', rv.data.decode('utf-8'))
        
        # 3. Financeiro: Update Expenses
        # Need to seed expenses first or assume they exist from init_db
        rv = self.app.post('/financeiro', data=dict(
            despesa_Agua=150.00,
            despesa_Luz=200.00
        ), follow_redirects=True)
        self.assertIn('Despesas atualizadas com sucesso', rv.data.decode('utf-8'))
        
        # 4. RH: Register Employee
        rv = self.app.post('/rh', data=dict(
            nome='Func Teste',
            cpf='11122233344',
            rg='1234567',
            endereco='Rua A',
            telefone='12345678',
            qtd_filhos=1,
            cargo='Operario',
            valor_hora=20.00
        ), follow_redirects=True)
        self.assertIn('Funcionário Func Teste cadastrado com sucesso', rv.data.decode('utf-8'))

    def test_hierarchical_rbac(self):
        # Setup users for hierarchy test
        self.login('admin', 'admin123')
        self.app.post('/users/create', data=dict(username='dir_operacional', password='password', role='diretor_operacional'))
        self.app.post('/users/create', data=dict(username='presidente', password='password', role='presidente'))
        self.app.post('/users/create', data=dict(username='func_producao', password='password', role='func_producao'))

        # 1. Diretor Operacional (Should access Operacional AND Estoque)
        self.login('dir_operacional', 'password')
        rv = self.app.get('/operacional')
        self.assertEqual(rv.status_code, 200)
        rv = self.app.get('/estoque')
        self.assertEqual(rv.status_code, 200)
        # Should NOT access Financeiro
        rv = self.app.get('/financeiro', follow_redirects=True)
        self.assertIn('Acesso negado', rv.data.decode('utf-8'))
        
        # 2. Presidente (Should access Everything)
        self.login('presidente', 'password')
        rv = self.app.get('/operacional')
        self.assertEqual(rv.status_code, 200)
        rv = self.app.get('/financeiro')
        self.assertEqual(rv.status_code, 200)
        
        # 3. Funcionario Produção (Only Operacional)
        self.login('func_producao', 'password')
        rv = self.app.get('/operacional')
        self.assertEqual(rv.status_code, 200)
        rv = self.app.get('/estoque', follow_redirects=True)
        self.assertIn('Acesso negado', rv.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
