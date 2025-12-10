"""
Testes de Integração Completos - Carangos S/A
Demonstra o fluxo completo: Produto → Produção → Finanças → RH
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from modules import estoque, operacional, financeiro, rh, data_manager
import time

console = Console()

def limpar_dados_teste():
    """Limpa dados de teste anteriores"""
    console.print("[yellow]🧹 Limpando dados de teste anteriores...[/yellow]")
    
    # Criar dados vazios para teste
    data_manager.save_data('produtos_teste.json', [])
    data_manager.save_data('producao_teste.json', [])
    data_manager.save_data('funcionarios_teste.json', [])
    data_manager.save_data('despesas_teste.json', [])
    
    console.print("[green]✅ Dados limpos com sucesso[/green]\n")

def teste_cadastrar_produtos():
    """Teste 1: Cadastrar produtos no estoque"""
    console.print(Panel.fit(
        "[bold cyan]📦 TESTE 1: CADASTRANDO PRODUTOS NO ESTOQUE[/bold cyan]",
        border_style="cyan"
    ))
    
    produtos = [
        {
            'codigo': 1001,
            'nome': 'Motor V8 Turbo',
            'data_fabricacao': '01/12/2024',
            'fornecedor': 'MotorTech Ltda',
            'quantidade': 50,
            'valor_compra': 15000.00
        },
        {
            'codigo': 1002,
            'nome': 'Chassi Reforçado',
            'data_fabricacao': '05/12/2024',
            'fornecedor': 'MetalForte S/A',
            'quantidade': 100,
            'valor_compra': 8000.00
        },
        {
            'codigo': 1003,
            'nome': 'Sistema de Freios ABS',
            'data_fabricacao': '08/12/2024',
            'fornecedor': 'SafeDrive Inc',
            'quantidade': 75,
            'valor_compra': 3500.00
        },
        {
            'codigo': 1004,
            'nome': 'Painel Digital Premium',
            'data_fabricacao': '10/12/2024',
            'fornecedor': 'TechAuto Brasil',
            'quantidade': 60,
            'valor_compra': 2800.00
        }
    ]
    
    # Salvar produtos
    data_manager.save_data('produtos.json', produtos)
    
    # Exibir tabela de produtos
    table = Table(title="✅ Produtos Cadastrados", box=box.ROUNDED)
    table.add_column("Código", style="cyan")
    table.add_column("Nome", style="green")
    table.add_column("Fornecedor", style="yellow")
    table.add_column("Qtd", style="magenta", justify="right")
    table.add_column("Valor Unit.", style="blue", justify="right")
    table.add_column("Total", style="bold green", justify="right")
    
    total_estoque = 0
    for p in produtos:
        total = p['quantidade'] * p['valor_compra']
        total_estoque += total
        table.add_row(
            str(p['codigo']),
            p['nome'],
            p['fornecedor'],
            str(p['quantidade']),
            f"R$ {p['valor_compra']:,.2f}",
            f"R$ {total:,.2f}"
        )
    
    console.print(table)
    console.print(f"\n[bold green]💰 Valor Total em Estoque: R$ {total_estoque:,.2f}[/bold green]\n")
    time.sleep(2)
    
    return produtos

def teste_registrar_producao():
    """Teste 2: Registrar produção semanal"""
    console.print(Panel.fit(
        "[bold cyan]🏭 TESTE 2: REGISTRANDO PRODUÇÃO SEMANAL[/bold cyan]",
        border_style="cyan"
    ))
    
    # Dados de produção simulados
    producao_semanal = [
        {"dia": "Segunda", "turno": "Manhã", "quantidade": 25},
        {"dia": "Segunda", "turno": "Tarde", "quantidade": 30},
        {"dia": "Segunda", "turno": "Noite", "quantidade": 22},
        {"dia": "Terça", "turno": "Manhã", "quantidade": 28},
        {"dia": "Terça", "turno": "Tarde", "quantidade": 32},
        {"dia": "Terça", "turno": "Noite", "quantidade": 24},
        {"dia": "Quarta", "turno": "Manhã", "quantidade": 26},
        {"dia": "Quarta", "turno": "Tarde", "quantidade": 31},
        {"dia": "Quarta", "turno": "Noite", "quantidade": 23},
        {"dia": "Quinta", "turno": "Manhã", "quantidade": 27},
        {"dia": "Quinta", "turno": "Tarde", "quantidade": 33},
        {"dia": "Quinta", "turno": "Noite", "quantidade": 25},
        {"dia": "Sexta", "turno": "Manhã", "quantidade": 29},
        {"dia": "Sexta", "turno": "Tarde", "quantidade": 34},
        {"dia": "Sexta", "turno": "Noite", "quantidade": 26},
        {"dia": "Sábado", "turno": "Manhã", "quantidade": 20},
        {"dia": "Sábado", "turno": "Tarde", "quantidade": 18},
        {"dia": "Sábado", "turno": "Noite", "quantidade": 15},
        {"dia": "Domingo", "turno": "Manhã", "quantidade": 10},
        {"dia": "Domingo", "turno": "Tarde", "quantidade": 8},
        {"dia": "Domingo", "turno": "Noite", "quantidade": 5},
    ]
    
    # Salvar produção
    data_manager.save_data('producao.json', producao_semanal)
    
    # Reconstruir estrutura para cálculos
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    dados_estruturados = []
    
    for dia in dias_semana:
        turnos_dia = {"Manhã": 0, "Tarde": 0, "Noite": 0}
        rows = [row for row in producao_semanal if row['dia'] == dia]
        for row in rows:
            if row['turno'] in turnos_dia:
                turnos_dia[row['turno']] += row['quantidade']
        dados_estruturados.append({"dia": dia, "turnos": turnos_dia})
    
    # Calcular estatísticas
    stats = operacional.calcular_estatisticas(dados_estruturados)
    ideal = operacional.calcular_capacidade_ideal(meta_mensal=750)
    
    # Exibir tabela de produção
    table = Table(title="✅ Produção Semanal Registrada", box=box.ROUNDED)
    table.add_column("Dia", style="cyan")
    table.add_column("Manhã", style="green", justify="right")
    table.add_column("Tarde", style="yellow", justify="right")
    table.add_column("Noite", style="blue", justify="right")
    table.add_column("Total", style="bold magenta", justify="right")
    
    for dia_data in dados_estruturados:
        dia = dia_data['dia']
        turnos = dia_data['turnos']
        total = sum(turnos.values())
        table.add_row(
            dia,
            str(turnos['Manhã']),
            str(turnos['Tarde']),
            str(turnos['Noite']),
            f"[bold]{total}[/bold]"
        )
    
    console.print(table)
    
    # Exibir estatísticas
    eficiencia = (stats['total_semanal'] / ideal['semanal']) * 100 if ideal['semanal'] > 0 else 0
    
    console.print(f"\n[bold cyan]📊 Estatísticas de Produção:[/bold cyan]")
    console.print(f"  Total Semanal: [bold]{stats['total_semanal']}[/bold] carros")
    console.print(f"  Média Diária: [bold]{stats['media_diaria']:.1f}[/bold] carros")
    console.print(f"  Meta Semanal: [bold]{ideal['semanal']:.1f}[/bold] carros")
    console.print(f"  Eficiência: [bold green]{eficiencia:.1f}%[/bold green]\n")
    time.sleep(2)
    
    return stats

def teste_calcular_financas(stats_producao):
    """Teste 3: Calcular indicadores financeiros"""
    console.print(Panel.fit(
        "[bold cyan]💰 TESTE 3: CALCULANDO INDICADORES FINANCEIROS[/bold cyan]",
        border_style="cyan"
    ))
    
    # Cadastrar despesas fixas
    despesas = [
        {'descricao': 'Aluguel da Fábrica', 'valor': 50000.00},
        {'descricao': 'Energia Elétrica', 'valor': 25000.00},
        {'descricao': 'Água e Saneamento', 'valor': 8000.00},
        {'descricao': 'Manutenção Equipamentos', 'valor': 15000.00},
        {'descricao': 'Segurança e Limpeza', 'valor': 12000.00}
    ]
    
    data_manager.save_data('despesas.json', despesas)
    
    # Calcular indicadores
    indicadores = financeiro.calcular_indicadores_financeiros()
    
    # Exibir tabela de despesas
    table = Table(title="✅ Despesas Fixas Cadastradas", box=box.ROUNDED)
    table.add_column("Descrição", style="cyan")
    table.add_column("Valor Mensal", style="green", justify="right")
    
    for desp in despesas:
        table.add_row(desp['descricao'], f"R$ {desp['valor']:,.2f}")
    
    console.print(table)
    
    # Exibir indicadores financeiros
    console.print(f"\n[bold cyan]📈 Indicadores Financeiros:[/bold cyan]")
    
    table2 = Table(box=box.SIMPLE)
    table2.add_column("Indicador", style="cyan")
    table2.add_column("Valor", style="green", justify="right")
    
    table2.add_row("Produção Total", f"{indicadores['total_produzido']} carros")
    table2.add_row("Custo Fixo Total", f"R$ {indicadores['custo_fixo_total']:,.2f}")
    table2.add_row("Custo Estoque", f"R$ {indicadores['custo_estoque_total']:,.2f}")
    table2.add_row("[bold]Custo Unitário[/bold]", f"[bold]R$ {indicadores['custo_unitario']:,.2f}[/bold]")
    table2.add_row("[bold cyan]Preço de Venda (+50%)[/bold cyan]", f"[bold cyan]R$ {indicadores['preco_venda']:,.2f}[/bold cyan]")
    table2.add_row("Lucro Bruto", f"R$ {indicadores['lucro_bruto']:,.2f}")
    table2.add_row("CSLL (9%)", f"[red]-R$ {indicadores['csll']:,.2f}[/red]")
    table2.add_row("[bold green]Lucro Líquido[/bold green]", f"[bold green]R$ {indicadores['lucro_liquido_final']:,.2f}[/bold green]")
    
    console.print(table2)
    console.print()
    time.sleep(2)
    
    return indicadores

def teste_gerenciar_rh():
    """Teste 4: Gerenciar funcionários e RH"""
    console.print(Panel.fit(
        "[bold cyan]👥 TESTE 4: GERENCIANDO RECURSOS HUMANOS[/bold cyan]",
        border_style="cyan"
    ))
    
    # Criar funcionários de teste
    funcionarios = [
        {
            'nome': 'João Silva',
            'cpf': '123.456.789-00',
            'rg': '12.345.678-9',
            'CTPS': '12345',
            'endereco': 'Rua das Flores 123',
            'telefone': '(11) 98765-4321',
            'qtd_filhos': 2,
            'cargo': 'Operador de Máquinas',
            'valor_hora': 8.50,
            'matricula': '120015',
            'data_cadastro': '10/12/2024 14:00:00'
        },
        {
            'nome': 'Maria Santos',
            'cpf': '987.654.321-00',
            'rg': '98.765.432-1',
            'CTPS': '54321',
            'endereco': 'Av Principal 456',
            'telefone': '(11) 91234-5678',
            'qtd_filhos': 1,
            'cargo': 'Inspetor de Qualidade',
            'valor_hora': 10.00,
            'matricula': '130027',
            'data_cadastro': '10/12/2024 14:05:00'
        },
        {
            'nome': 'Pedro Oliveira',
            'cpf': '456.789.123-00',
            'rg': '45.678.912-3',
            'CTPS': '67890',
            'endereco': 'Rua Central 789',
            'telefone': '(11) 95555-1234',
            'qtd_filhos': 0,
            'cargo': 'Analista Financeiro',
            'valor_hora': 12.50,
            'matricula': '320013',
            'data_cadastro': '10/12/2024 14:10:00'
        },
        {
            'nome': 'Ana Costa',
            'cpf': '321.654.987-00',
            'rg': '32.165.498-7',
            'CTPS': '98765',
            'endereco': 'Rua Nova 321',
            'telefone': '(11) 94444-9876',
            'qtd_filhos': 3,
            'cargo': 'Analista de RH',
            'valor_hora': 11.50,
            'matricula': '420029',
            'data_cadastro': '10/12/2024 14:15:00'
        }
    ]
    
    # Salvar funcionários
    data_manager.save_data('funcionarios.json', funcionarios)
    
    # Exibir tabela de funcionários
    table = Table(title="✅ Funcionários Cadastrados", box=box.ROUNDED)
    table.add_column("Matrícula", style="cyan")
    table.add_column("Nome", style="green")
    table.add_column("Cargo", style="yellow")
    table.add_column("Valor/Hora", style="magenta", justify="right")
    table.add_column("Filhos", style="blue", justify="center")
    
    total_folha = 0
    for func in funcionarios:
        salario_base = func['valor_hora'] * 220  # 220 horas/mês
        total_folha += salario_base
        table.add_row(
            func['matricula'],
            func['nome'],
            func['cargo'],
            f"R$ {func['valor_hora']:.2f}",
            str(func['qtd_filhos'])
        )
    
    console.print(table)
    
    # Resumo da folha
    console.print(f"\n[bold cyan]💼 Resumo da Folha de Pagamento:[/bold cyan]")
    console.print(f"  Total de Funcionários: [bold]{len(funcionarios)}[/bold]")
    console.print(f"  Folha Base (220h): [bold green]R$ {total_folha:,.2f}[/bold green]")
    
    # Distribuição por setor
    setores = {}
    for func in funcionarios:
        # Determinar setor pelo cargo
        if 'Operador' in func['cargo'] or 'Inspetor' in func['cargo'] or 'Técnico' in func['cargo']:
            setor = 'OPERACIONAL'
        elif 'Estoque' in func['cargo']:
            setor = 'ESTOQUE'
        elif 'Financeiro' in func['cargo']:
            setor = 'FINANCEIRO'
        elif 'RH' in func['cargo']:
            setor = 'RH'
        else:
            setor = 'OUTROS'
        
        setores[setor] = setores.get(setor, 0) + 1
    
    console.print(f"\n[bold cyan]📊 Distribuição por Setor:[/bold cyan]")
    for setor, count in setores.items():
        console.print(f"  {setor}: [bold]{count}[/bold] funcionário(s)")
    
    console.print()
    time.sleep(2)
    
    return funcionarios

def executar_teste_completo():
    """Executa o teste de integração completo"""
    console.clear()
    console.print(Panel.fit(
        "[bold cyan]🚀 TESTE DE INTEGRAÇÃO COMPLETO - CARANGOS S/A[/bold cyan]\n"
        "[yellow]Demonstração do fluxo completo do sistema[/yellow]",
        border_style="cyan"
    ))
    console.print()
    
    try:
        # Limpar dados anteriores
        limpar_dados_teste()
        
        # Teste 1: Cadastrar Produtos
        produtos = teste_cadastrar_produtos()
        
        # Teste 2: Registrar Produção
        stats_producao = teste_registrar_producao()
        
        # Teste 3: Calcular Finanças
        indicadores = teste_calcular_financas(stats_producao)
        
        # Teste 4: Gerenciar RH
        funcionarios = teste_gerenciar_rh()
        
        # Resumo Final
        console.print(Panel.fit(
            "[bold green]✅ TESTE DE INTEGRAÇÃO CONCLUÍDO COM SUCESSO![/bold green]\n\n"
            f"[cyan]📦 Produtos Cadastrados:[/cyan] {len(produtos)}\n"
            f"[cyan]🏭 Carros Produzidos:[/cyan] {stats_producao['total_semanal']}\n"
            f"[cyan]💰 Lucro Líquido:[/cyan] R$ {indicadores['lucro_liquido_final']:,.2f}\n"
            f"[cyan]👥 Funcionários:[/cyan] {len(funcionarios)}",
            title="🎉 Resumo Final",
            border_style="green"
        ))
        
        console.print("\n[bold]O sistema está funcionando perfeitamente![/bold] 🚗✨\n")
        
    except Exception as e:
        console.print(f"\n[red]❌ Erro durante o teste: {e}[/red]")
        import traceback
        console.print(traceback.format_exc())

if __name__ == "__main__":
    executar_teste_completo()
