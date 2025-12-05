
from flask import Flask, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import modules
from modules import data_manager, operacional, estoque, financeiro, rh

app = Flask(__name__)
# Use environment variable for secret key, with fallback for development
app.secret_key = os.getenv('SECRET_KEY', 'dev-key-only-change-in-production')

def init_db():
    # Initialize JSON files if empty
    if not data_manager.load_data('despesas.json'):
        default_expenses = [
            {'tipo': 'Agua', 'valor': 0.0},
            {'tipo': 'Luz', 'valor': 0.0},
            {'tipo': 'Salarios', 'valor': 0.0},
            {'tipo': 'Impostos', 'valor': 0.0}
        ]
        data_manager.save_data('despesas.json', default_expenses)
    
    # Ensure users.json exists (seeded by seed_users.py, but good to have check)
    if not data_manager.load_data('users.json'):
        # Create default admin if completely empty
        admin_pass = generate_password_hash('admin123')
        data_manager.save_data('users.json', [{'username': 'admin', 'password': admin_pass, 'role': 'admin'}])

# Role Definitions based on Organogram
ROLES_GLOBAL = ['admin', 'presidente', 'conselho']
ROLES_OPERACIONAL = ROLES_GLOBAL + ['diretor_operacional', 'gerente_montagem', 'func_producao']
ROLES_ESTOQUE = ROLES_GLOBAL + ['diretor_operacional', 'gerente_insumos', 'func_estoque']
ROLES_FINANCEIRO = ROLES_GLOBAL + ['diretor_financeiro', 'gerente_financeiro', 'func_financeiro']
ROLES_RH = ROLES_GLOBAL + ['diretor_rh', 'gerente_rh', 'func_rh']

# Decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, faça login para acessar.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('login'))
            
            user_role = session.get('role')
            # Check if user has one of the allowed roles
            if user_role not in allowed_roles:
                flash('Acesso negado. Você não tem permissão para acessar esta área.', 'danger')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = data_manager.load_data('users.json')
        user = next((u for u in users if u['username'] == username), None)
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['username'] # Use username as ID for JSON
            session['username'] = user['username']
            session['role'] = user['role']
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')
            
    return render_template('auth/login.html')

@app.route('/users/create', methods=['GET', 'POST'])
@login_required
@role_required(ROLES_RH)
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form.get('role', 'user')
        
        users = data_manager.load_data('users.json')
        
        if any(u['username'] == username for u in users):
            flash('Usuário já existe.', 'danger')
        else:
            hashed_password = generate_password_hash(password)
            users.append({
                'username': username,
                'password': hashed_password,
                'role': role
            })
            data_manager.save_data('users.json', users)
            flash(f'Usuário {username} criado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
            
    return render_template('users/create.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_role = session.get('role')
    
    # Data for Executive View (Global Roles)
    stats = {}
    if user_role in ROLES_GLOBAL:
        # 1. Produção Semanal
        producao = data_manager.load_data('producao.json')
        stats['total_semanal'] = sum(row['quantidade'] for row in producao)
        
        # 2. Custo Total Produção (Fixas + Insumos)
        despesas = data_manager.load_data('despesas.json')
        total_fixo = sum(d['valor'] for d in despesas)
        
        produtos = data_manager.load_data('produtos.json')
        custo_insumos = sum(p['quantidade'] * p['valor_compra'] for p in produtos)
        
        stats['custo_total_producao'] = financeiro.calcular_custo_producao(total_fixo, custo_insumos)
        
        # 3. Preço Venda Sugerido
        qtd_carros = stats['total_semanal'] 
        custo_unitario = financeiro.calcular_custo_por_carro(stats['custo_total_producao'], qtd_carros)
        stats['preco_venda'] = financeiro.calcular_preco_venda(custo_unitario)
        
        # 4. Funcionários
        funcionarios = data_manager.load_data('funcionarios.json')
        stats['qtd_funcionarios'] = len(funcionarios)
        
    return render_template('dashboard.html', 
                           user=session['username'], 
                           role=user_role,
                           **stats)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=session['username'], role=session['role'])

# Module Routes with RBAC

@app.route('/operacional', methods=['GET', 'POST'])
@login_required
@role_required(ROLES_OPERACIONAL)
def mod_operacional():
    if request.method == 'POST':
        dia = request.form['dia']
        turno = request.form['turno']
        try:
            quantidade = int(request.form['quantidade'])
            if quantidade < 0:
                flash('Quantidade não pode ser negativa.', 'warning')
            else:
                # Load, Append, Save
                producao = data_manager.load_data('producao.json')
                producao.append({
                    'dia': dia,
                    'turno': turno,
                    'quantidade': quantidade
                })
                data_manager.save_data('producao.json', producao)
                flash('Produção registrada com sucesso!', 'success')
        except ValueError:
            flash('Quantidade inválida.', 'danger')
    
    # Fetch data for report
    producao_db = data_manager.load_data('producao.json')
    
    # Transform for statistics
    dados_formatados = []
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    
    for dia in dias_semana:
        turnos_dia = {"Manhã": 0, "Tarde": 0, "Noite": 0}
        rows = [row for row in producao_db if row['dia'] == dia]
        for row in rows:
            if row['turno'] in turnos_dia:
                turnos_dia[row['turno']] += row['quantidade']
        
        dados_formatados.append({"dia": dia, "turnos": turnos_dia})
        
    # Use Core Module Functions
    stats = operacional.calcular_estatisticas(dados_formatados)
    ideal = operacional.calcular_capacidade_ideal()
    mensal_est, anual_est = operacional.simular_producao(stats['total_semanal'])
    
    return render_template('modules/operacional.html', 
                           producao=producao_db, 
                           total_semanal=stats['total_semanal'],
                           total_turnos=stats['total_por_turno'],
                           media_diaria=stats['media_diaria'],
                           mensal_est=mensal_est,
                           anual_est=anual_est,
                           ideal=ideal)

@app.route('/estoque', methods=['GET', 'POST'])
@login_required
@role_required(ROLES_ESTOQUE)
def mod_estoque():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']
        data_fab = request.form['data_fabricacao']
        fornecedor = request.form['fornecedor']
        try:
            quantidade = int(request.form['quantidade'])
            valor_compra = float(request.form['valor_compra'])
            
            produtos = data_manager.load_data('produtos.json')
            
            # Check duplicate
            exists = any(p['codigo'] == codigo for p in produtos)
            if exists:
                flash(f'Produto com código {codigo} já existe.', 'danger')
            else:
                produtos.append({
                    'codigo': codigo,
                    'nome': nome,
                    'data_fabricacao': data_fab,
                    'fornecedor': fornecedor,
                    'quantidade': quantidade,
                    'valor_compra': valor_compra
                })
                data_manager.save_data('produtos.json', produtos)
                flash(f'Produto {nome} cadastrado com sucesso!', 'success')
        except ValueError:
            flash('Valores inválidos para quantidade ou preço.', 'danger')
            
    # Fetch products
    produtos_db = data_manager.load_data('produtos.json')
    
    # Use Core Module Function
    custos = estoque.calcular_custos(produtos_db)
    
    return render_template('modules/estoque.html', 
                           produtos=produtos_db,
                           custo_total_atual=custos['total_atual'],
                           custo_mensal=custos['mensal_projetado'],
                           custo_anual=custos['anual_projetado'])

@app.route('/financeiro', methods=['GET', 'POST'])
@login_required
@role_required(ROLES_FINANCEIRO)
def mod_financeiro():
    if request.method == 'POST':
        try:
            despesas = data_manager.load_data('despesas.json')
            # Update expenses
            for key in request.form:
                if key.startswith('despesa_'):
                    tipo = key.replace('despesa_', '')
                    valor = float(request.form[key])
                    # Update in list
                    for d in despesas:
                        if d['tipo'] == tipo:
                            d['valor'] = valor
            data_manager.save_data('despesas.json', despesas)
            flash('Despesas atualizadas com sucesso!', 'success')
        except ValueError:
            flash('Valores inválidos.', 'danger')
            
    # Fetch expenses
    despesas = data_manager.load_data('despesas.json')
    total_fixo = sum(d['valor'] for d in despesas)
    
    # Fetch production cost (Insumos) from Estoque
    produtos = data_manager.load_data('produtos.json')
    custo_insumos = sum(p['quantidade'] * p['valor_compra'] for p in produtos)
    
    # Fetch production quantity from Operacional
    producao = data_manager.load_data('producao.json')
    qtd_carros = sum(row['quantidade'] for row in producao)
    
    # Calculations
    custo_total_producao = financeiro.calcular_custo_producao(total_fixo, custo_insumos)
    custo_unitario = financeiro.calcular_custo_por_carro(custo_total_producao, qtd_carros)
    preco_venda = financeiro.calcular_preco_venda(custo_unitario)
    
    return render_template('modules/financeiro.html', 
                           despesas=despesas,
                           total_fixo=total_fixo,
                           custo_insumos=custo_insumos,
                           custo_total_producao=custo_total_producao,
                           qtd_carros=qtd_carros,
                           custo_unitario=custo_unitario,
                           preco_venda=preco_venda)

@app.route('/rh', methods=['GET', 'POST'])
@login_required
@role_required(ROLES_RH)
def mod_rh():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        rg = request.form['rg']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        cargo = request.form['cargo']
        try:
            qtd_filhos = int(request.form['qtd_filhos'])
            valor_hora = float(request.form['valor_hora'])
            
            funcionarios = data_manager.load_data('funcionarios.json')
            
            # Check duplicate CPF
            exists = any(f['cpf'] == cpf for f in funcionarios)
            if exists:
                flash(f'Funcionário com CPF {cpf} já existe.', 'danger')
            else:
                funcionarios.append({
                    'nome': nome,
                    'cpf': cpf,
                    'rg': rg,
                    'endereco': endereco,
                    'telefone': telefone,
                    'qtd_filhos': qtd_filhos,
                    'cargo': cargo,
                    'valor_hora': valor_hora
                })
                data_manager.save_data('funcionarios.json', funcionarios)
                flash(f'Funcionário {nome} cadastrado com sucesso!', 'success')
        except ValueError:
            flash('Valores inválidos.', 'danger')
            
    # Fetch employees
    funcionarios = data_manager.load_data('funcionarios.json')
    funcionarios.sort(key=lambda x: x['nome'])
    
    # Generate Payroll Data
    folha = []
    for f in funcionarios:
        # Simulation: 160h regular + 10h overtime
        horas_trab = 160
        horas_ext = 10
        
        bruto = rh.calcular_salario_bruto(horas_trab, f['valor_hora'])
        extra = rh.calcular_horas_extras(horas_ext, f['valor_hora'], f['cargo'])
        total_bruto = bruto + extra
        
        irpf = rh.calcular_irpf(total_bruto)
        liquido = rh.calcular_liquido(total_bruto, irpf)
        
        folha.append({
            'nome': f['nome'],
            'cargo': f['cargo'],
            'bruto': total_bruto,
            'irpf': irpf,
            'liquido': liquido
        })
    
    return render_template('modules/rh.html', 
                           funcionarios=funcionarios,
                           folha=folha)

@app.route('/terminal')
@login_required
def terminal():
    """Terminal interativo na interface web"""
    return render_template('terminal.html', user=session['username'], role=session['role'])

@app.route('/terminal/execute', methods=['POST'])
@login_required
def terminal_execute():
    """Executa comandos do terminal e retorna resultado em JSON"""
    from flask import jsonify
    
    command = request.json.get('command', '').strip().lower()
    user_role = session.get('role')
    
    # Comandos disponíveis
    if command == 'help' or command == 'ajuda':
        return jsonify({
            'output': '''
<span class="text-primary">Comandos Disponíveis:</span>

<span class="text-success">Geral:</span>
  help, ajuda          - Mostra esta ajuda
  clear, limpar        - Limpa a tela
  status               - Mostra informações do sistema
  whoami               - Mostra usuário atual

<span class="text-success">CLI (Interface de Linha de Comando):</span>
  main                 - Menu principal do sistema CLI
  main operacional     - Menu do módulo operacional
  main estoque         - Menu do módulo de estoque
  main financeiro      - Menu do módulo financeiro
  main rh              - Menu do módulo de RH

<span class="text-success">Operacional:</span>
  producao             - Mostra relatório de produção
  
<span class="text-success">Estoque:</span>
  estoque              - Mostra relatório de estoque
  produtos             - Lista todos os produtos
  
<span class="text-success">Financeiro:</span>
  financeiro           - Mostra relatório financeiro
  despesas             - Lista despesas fixas
  
<span class="text-success">RH:</span>
  rh                   - Mostra relatório de RH
  funcionarios         - Lista todos os funcionários
  folha                - Mostra folha de pagamento
''',
            'type': 'success'
        })

    
    elif command == 'clear' or command == 'limpar':
        return jsonify({'output': '', 'type': 'clear'})
    
    elif command == 'whoami':
        return jsonify({
            'output': f'<span class="text-info">Usuário:</span> {session["username"]}\n<span class="text-info">Cargo:</span> {user_role}',
            'type': 'info'
        })
    
    elif command == 'status':
        producao = data_manager.load_data('producao.json')
        produtos = data_manager.load_data('produtos.json')
        funcionarios = data_manager.load_data('funcionarios.json')
        
        total_producao = sum(row['quantidade'] for row in producao)
        total_produtos = len(produtos)
        total_funcionarios = len(funcionarios)
        
        return jsonify({
            'output': f'''
<span class="text-primary">═══ STATUS DO SISTEMA ═══</span>

<span class="text-success">Produção Total:</span> {total_producao} unidades
<span class="text-success">Produtos Cadastrados:</span> {total_produtos}
<span class="text-success">Funcionários:</span> {total_funcionarios}
<span class="text-success">Usuário:</span> {session["username"]} ({user_role})
''',
            'type': 'success'
        })
    
    elif command == 'producao':
        if user_role not in ROLES_OPERACIONAL:
            return jsonify({'output': '<span class="text-danger">Acesso negado! Você não tem permissão para este comando.</span>', 'type': 'error'})
        
        dados_flat = data_manager.load_data('producao.json')
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        dados_estruturados = []
        
        for dia in dias_semana:
            turnos_dia = {"Manhã": 0, "Tarde": 0, "Noite": 0}
            rows = [row for row in dados_flat if row['dia'] == dia]
            for row in rows:
                if row['turno'] in turnos_dia:
                    turnos_dia[row['turno']] += row['quantidade']
            dados_estruturados.append({"dia": dia, "turnos": turnos_dia})
        
        stats = operacional.calcular_estatisticas(dados_estruturados)
        ideal = operacional.calcular_capacidade_ideal()
        
        output = f'''
<span class="text-primary">═══ RELATÓRIO DE PRODUÇÃO ═══</span>

<span class="text-success">Total Semanal:</span> {stats['total_semanal']} unidades
<span class="text-success">Média Diária:</span> {stats['media_diaria']:.1f} unidades
<span class="text-success">Capacidade Ideal:</span> {ideal} unidades/semana

<span class="text-info">Por Turno:</span>
  Manhã: {stats['total_por_turno']['Manhã']} unidades
  Tarde: {stats['total_por_turno']['Tarde']} unidades
  Noite: {stats['total_por_turno']['Noite']} unidades
'''
        return jsonify({'output': output, 'type': 'success'})
    
    elif command == 'estoque' or command == 'produtos':
        if user_role not in ROLES_ESTOQUE:
            return jsonify({'output': '<span class="text-danger">Acesso negado! Você não tem permissão para este comando.</span>', 'type': 'error'})
        
        produtos = data_manager.load_data('produtos.json')
        custos = estoque.calcular_custos(produtos)
        
        output = f'''
<span class="text-primary">═══ RELATÓRIO DE ESTOQUE ═══</span>

<span class="text-success">Total de Produtos:</span> {len(produtos)}
<span class="text-success">Custo Total:</span> R$ {custos['total_atual']:.2f}
<span class="text-success">Custo Mensal Projetado:</span> R$ {custos['mensal_projetado']:.2f}
<span class="text-success">Custo Anual Projetado:</span> R$ {custos['anual_projetado']:.2f}

<span class="text-info">Produtos:</span>
'''
        for p in produtos[:10]:  # Limita a 10 produtos
            output += f"  [{p['codigo']}] {p['nome']} - Qtd: {p['quantidade']} - R$ {p['valor_compra']:.2f}\n"
        
        if len(produtos) > 10:
            output += f"\n  ... e mais {len(produtos) - 10} produtos"
        
        return jsonify({'output': output, 'type': 'success'})
    
    elif command == 'financeiro' or command == 'despesas':
        if user_role not in ROLES_FINANCEIRO:
            return jsonify({'output': '<span class="text-danger">Acesso negado! Você não tem permissão para este comando.</span>', 'type': 'error'})
        
        despesas = data_manager.load_data('despesas.json')
        total_fixo = sum(d['valor'] for d in despesas)
        
        produtos = data_manager.load_data('produtos.json')
        custo_insumos = sum(p['quantidade'] * p['valor_compra'] for p in produtos)
        
        producao = data_manager.load_data('producao.json')
        qtd_carros = sum(row['quantidade'] for row in producao)
        
        custo_total = financeiro.calcular_custo_producao(total_fixo, custo_insumos)
        custo_unitario = financeiro.calcular_custo_por_carro(custo_total, qtd_carros) if qtd_carros > 0 else 0
        preco_venda = financeiro.calcular_preco_venda(custo_unitario)
        
        output = f'''
<span class="text-primary">═══ RELATÓRIO FINANCEIRO ═══</span>

<span class="text-success">Despesas Fixas:</span> R$ {total_fixo:.2f}
<span class="text-success">Custo Insumos:</span> R$ {custo_insumos:.2f}
<span class="text-success">Custo Total Produção:</span> R$ {custo_total:.2f}
<span class="text-success">Produção Total:</span> {qtd_carros} unidades
<span class="text-success">Custo Unitário:</span> R$ {custo_unitario:.2f}
<span class="text-success">Preço Venda Sugerido:</span> R$ {preco_venda:.2f}

<span class="text-info">Despesas Detalhadas:</span>
'''
        for d in despesas:
            output += f"  {d['tipo']}: R$ {d['valor']:.2f}\n"
        
        return jsonify({'output': output, 'type': 'success'})
    
    elif command == 'rh' or command == 'funcionarios' or command == 'folha':
        if user_role not in ROLES_RH:
            return jsonify({'output': '<span class="text-danger">Acesso negado! Você não tem permissão para este comando.</span>', 'type': 'error'})
        
        funcionarios = data_manager.load_data('funcionarios.json')
        
        output = f'''
<span class="text-primary">═══ RELATÓRIO DE RH ═══</span>

<span class="text-success">Total de Funcionários:</span> {len(funcionarios)}

<span class="text-info">Funcionários:</span>
'''
        for f in funcionarios:
            # Simulação de cálculo
            horas_trab = 160
            horas_ext = 10
            bruto = rh.calcular_salario_bruto(horas_trab, f['valor_hora'])
            extra = rh.calcular_horas_extras(horas_ext, f['valor_hora'], f['cargo'])
            total_bruto = bruto + extra
            irpf = rh.calcular_irpf(total_bruto)
            liquido = rh.calcular_liquido(total_bruto, irpf)
            
            output += f"  {f['nome']} ({f['cargo']}) - Líquido: R$ {liquido:.2f}\n"
        
        return jsonify({'output': output, 'type': 'success'})
    
    elif command.startswith('main'):
        parts = command.split()
        
        if len(parts) == 1:
            # Mostra menu principal do CLI
            return jsonify({
                'output': '''
<span class="text-primary">═══ SISTEMA CLI - MENU PRINCIPAL ═══</span>

<span class="text-success">Módulos Disponíveis:</span>
  <span class="text-info">main operacional</span>    - Módulo Operacional
  <span class="text-info">main estoque</span>        - Módulo de Estoque
  <span class="text-info">main financeiro</span>     - Módulo Financeiro
  <span class="text-info">main rh</span>             - Módulo de RH

<span class="text-warning">Dica:</span> Use os comandos diretos (producao, estoque, etc.) para relatórios rápidos
<span class="text-warning">Exemplo:</span> Digite "main operacional" para ver opções do módulo operacional
''',
                'type': 'success'
            })
        
        elif len(parts) == 2:
            modulo = parts[1].lower()
            
            if modulo == 'operacional':
                if user_role not in ROLES_OPERACIONAL:
                    return jsonify({'output': '<span class="text-danger">Acesso negado! Você não tem permissão para este módulo.</span>', 'type': 'error'})
                
                return jsonify({
                    'output': '''
<span class="text-primary">═══ MÓDULO OPERACIONAL ═══</span>

<span class="text-success">Opções Disponíveis:</span>
  <span class="text-info">producao</span>             - Ver relatório de produção semanal
  <span class="text-info">status</span>               - Ver status geral do sistema

<span class="text-warning">Funcionalidades do CLI:</span>
  • Registrar produção semanal
  • Ver relatórios detalhados de produção
  • Calcular capacidade ideal vs real
  • Projeções mensais e anuais

<span class="text-info">Use o comando "producao" para ver o relatório completo</span>
''',
                    'type': 'success'
                })
            
            elif modulo == 'estoque':
                if user_role not in ROLES_ESTOQUE:
                    return jsonify({'output': '<span class="text-danger">Acesso negado! Você não tem permissão para este módulo.</span>', 'type': 'error'})
                
                return jsonify({
                    'output': '''
<span class="text-primary">═══ MÓDULO DE ESTOQUE ═══</span>

<span class="text-success">Opções Disponíveis:</span>
  <span class="text-info">estoque</span>              - Ver relatório de estoque
  <span class="text-info">produtos</span>             - Listar todos os produtos

<span class="text-warning">Funcionalidades do CLI:</span>
  • Cadastrar novos produtos
  • Buscar produtos por código ou nome
  • Ver relatório de custos (atual, mensal, anual)
  • Controlar quantidade em estoque

<span class="text-info">Use o comando "estoque" para ver o relatório completo</span>
''',
                    'type': 'success'
                })
            
            elif modulo == 'financeiro':
                if user_role not in ROLES_FINANCEIRO:
                    return jsonify({'output': '<span class="text-danger">Acesso negado! Você não tem permissão para este módulo.</span>', 'type': 'error'})
                
                return jsonify({
                    'output': '''
<span class="text-primary">═══ MÓDULO FINANCEIRO ═══</span>

<span class="text-success">Opções Disponíveis:</span>
  <span class="text-info">financeiro</span>           - Ver relatório financeiro completo
  <span class="text-info">despesas</span>             - Ver despesas fixas

<span class="text-warning">Funcionalidades do CLI:</span>
  • Gerenciar despesas fixas (Água, Luz, Salários, Impostos)
  • Calcular custo total de produção
  • Calcular custo unitário por carro
  • Calcular preço de venda sugerido (+50%)

<span class="text-info">Use o comando "financeiro" para ver o relatório completo</span>
''',
                    'type': 'success'
                })
            
            elif modulo == 'rh':
                if user_role not in ROLES_RH:
                    return jsonify({'output': '<span class="text-danger">Acesso negado! Você não tem permissão para este módulo.</span>', 'type': 'error'})
                
                return jsonify({
                    'output': '''
<span class="text-primary">═══ MÓDULO DE RH ═══</span>

<span class="text-success">Opções Disponíveis:</span>
  <span class="text-info">rh</span>                   - Ver relatório de RH
  <span class="text-info">funcionarios</span>         - Listar todos os funcionários
  <span class="text-info">folha</span>                - Ver folha de pagamento

<span class="text-warning">Funcionalidades do CLI:</span>
  • Cadastrar novos funcionários
  • Ver folha de pagamento simulada
  • Calcular salário bruto + horas extras
  • Calcular IRPF e salário líquido
  • Gerenciar dados de funcionários

<span class="text-info">Use o comando "rh" para ver o relatório completo</span>
''',
                    'type': 'success'
                })
            
            else:
                return jsonify({
                    'output': f'<span class="text-danger">Módulo "{modulo}" não reconhecido.</span>\nMódulos disponíveis: operacional, estoque, financeiro, rh',
                    'type': 'error'
                })
        
        else:
            return jsonify({
                'output': '<span class="text-danger">Uso incorreto do comando.</span>\nUso: main [modulo]\nExemplo: main operacional',
                'type': 'error'
            })
    
    else:
        return jsonify({
            'output': f'<span class="text-danger">Comando não reconhecido: "{command}"</span>\nDigite "help" para ver os comandos disponíveis.',
            'type': 'error'
        })



if __name__ == '__main__':
    init_db()
    # Get configuration from environment variables
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'production') == 'development'
    
    # Run with host 0.0.0.0 to allow external connections (required for cloud)
    app.run(host='0.0.0.0', port=port, debug=debug)

