"""
APRESENTAÇÃO COMPLETA - SISTEMA CARANGOS S/A
Demonstração unificada de todos os módulos e funcionalidades
Perfeito para apresentação em sala de aula
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich import box
from modules import estoque, operacional, financeiro, rh, data_manager
import time

console = Console()

class ApresentacaoCarangos:
    """Classe principal para apresentação do sistema"""
    
    def __init__(self):
        self.produtos = []
        self.producao = []
        self.funcionarios = []
        self.despesas = []
    
    def exibir_cabecalho(self):
        """Exibe o cabeçalho da apresentação"""
        console.clear()
        console.print(Panel.fit(
            "[bold cyan]🚗 SISTEMA CARANGOS S/A[/bold cyan]\n"
            "[yellow]Apresentação Completa do Sistema de Gestão[/yellow]\n\n"
            "[white]Módulos:[/white] Operacional | Estoque | Financeiro | RH",
            border_style="cyan",
            title="🏭 Fábrica de Automóveis"
        ))
        console.print()
        time.sleep(2)
    
    def modulo_1_estoque(self):
        """Módulo 1: Gestão de Estoque"""
        console.print(Panel.fit(
            "[bold green]📦 MÓDULO 1: GESTÃO DE ESTOQUE[/bold green]",
            border_style="green"
        ))
        console.print()
        
        # Cadastrar produtos
        self.produtos = [
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
        
        data_manager.save_data('produtos.json', self.produtos)
        
        # Exibir tabela
        table = Table(title="✅ Produtos em Estoque", box=box.ROUNDED, show_header=True)
        table.add_column("Código", style="cyan", width=8)
        table.add_column("Produto", style="green", width=25)
        table.add_column("Fornecedor", style="yellow", width=20)
        table.add_column("Qtd", style="magenta", justify="right", width=6)
        table.add_column("Valor Unit.", style="blue", justify="right", width=14)
        table.add_column("Total", style="bold green", justify="right", width=16)
        
        total_estoque = 0
        for p in self.produtos:
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
        console.print(f"\n[bold green]💰 Investimento Total em Estoque: R$ {total_estoque:,.2f}[/bold green]")
        console.print(f"[cyan]📊 Total de Produtos Cadastrados: {len(self.produtos)}[/cyan]\n")
        
        input("[yellow]Pressione ENTER para continuar...[/yellow]")
        console.clear()
    
    def modulo_2_producao(self):
        """Módulo 2: Controle de Produção"""
        console.print(Panel.fit(
            "[bold blue]🏭 MÓDULO 2: CONTROLE DE PRODUÇÃO[/bold blue]",
            border_style="blue"
        ))
        console.print()
        
        # Dados de produção
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
        
        data_manager.save_data('producao.json', producao_semanal)
        
        # Estruturar dados
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        dados_estruturados = []
        
        for dia in dias_semana:
            turnos_dia = {"Manhã": 0, "Tarde": 0, "Noite": 0}
            for row in producao_semanal:
                if row['dia'] == dia and row['turno'] in turnos_dia:
                    turnos_dia[row['turno']] += row['quantidade']
            dados_estruturados.append({"dia": dia, "turnos": turnos_dia})
        
        # Calcular estatísticas
        stats = operacional.calcular_estatisticas(dados_estruturados)
        ideal = operacional.calcular_capacidade_ideal(meta_mensal=750)
        eficiencia = (stats['total_semanal'] / ideal['semanal']) * 100 if ideal['semanal'] > 0 else 0
        
        # Exibir tabela
        table = Table(title="✅ Produção Semanal", box=box.ROUNDED)
        table.add_column("Dia", style="cyan", width=10)
        table.add_column("Manhã", style="green", justify="right", width=8)
        table.add_column("Tarde", style="yellow", justify="right", width=8)
        table.add_column("Noite", style="blue", justify="right", width=8)
        table.add_column("Total", style="bold magenta", justify="right", width=8)
        
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
        
        # Estatísticas
        console.print(f"\n[bold cyan]📊 Estatísticas de Produção:[/bold cyan]")
        console.print(f"  🚗 Total Semanal: [bold]{stats['total_semanal']}[/bold] carros")
        console.print(f"  📈 Média Diária: [bold]{stats['media_diaria']:.1f}[/bold] carros/dia")
        console.print(f"  🎯 Meta Semanal: [bold]{ideal['semanal']:.0f}[/bold] carros")
        console.print(f"  ⚡ Eficiência: [bold green]{eficiencia:.1f}%[/bold green]")
        
        if eficiencia >= 100:
            console.print(f"\n[bold green]✅ META SUPERADA! Produção {eficiencia - 100:.1f}% acima do esperado![/bold green]\n")
        else:
            console.print(f"\n[yellow]⚠️ Atenção: Produção {100 - eficiencia:.1f}% abaixo da meta[/yellow]\n")
        
        input("[yellow]Pressione ENTER para continuar...[/yellow]")
        console.clear()
    
    def modulo_3_financeiro(self):
        """Módulo 3: Gestão Financeira"""
        console.print(Panel.fit(
            "[bold yellow]💰 MÓDULO 3: GESTÃO FINANCEIRA[/bold yellow]",
            border_style="yellow"
        ))
        console.print()
        
        # Despesas
        self.despesas = [
            {'descricao': 'Aluguel da Fábrica', 'valor': 50000.00},
            {'descricao': 'Energia Elétrica', 'valor': 25000.00},
            {'descricao': 'Água e Saneamento', 'valor': 8000.00},
            {'descricao': 'Manutenção Equipamentos', 'valor': 15000.00},
            {'descricao': 'Segurança e Limpeza', 'valor': 12000.00}
        ]
        
        data_manager.save_data('despesas.json', self.despesas)
        
        # Calcular indicadores
        indicadores = financeiro.calcular_indicadores_financeiros()
        
        # Tabela de despesas
        table1 = Table(title="💸 Despesas Fixas Mensais", box=box.ROUNDED)
        table1.add_column("Descrição", style="cyan", width=30)
        table1.add_column("Valor", style="red", justify="right", width=16)
        
        total_despesas = 0
        for desp in self.despesas:
            total_despesas += desp['valor']
            table1.add_row(desp['descricao'], f"R$ {desp['valor']:,.2f}")
        
        table1.add_row("[bold]TOTAL[/bold]", f"[bold red]R$ {total_despesas:,.2f}[/bold red]")
        console.print(table1)
        
        # Indicadores financeiros
        console.print(f"\n[bold cyan]📈 Indicadores Financeiros:[/bold cyan]\n")
        
        table2 = Table(box=box.SIMPLE, show_header=False)
        table2.add_column("Indicador", style="cyan", width=35)
        table2.add_column("Valor", style="green", justify="right", width=20)
        
        table2.add_row("🚗 Produção Total", f"{indicadores['total_produzido']} carros")
        table2.add_row("💵 Custo Fixo Total", f"R$ {indicadores['custo_fixo_total']:,.2f}")
        table2.add_row("📦 Custo de Estoque", f"R$ {indicadores['custo_estoque_total']:,.2f}")
        table2.add_row("[bold]💎 Custo Unitário[/bold]", f"[bold]R$ {indicadores['custo_unitario']:,.2f}[/bold]")
        table2.add_row("[bold cyan]🏷️ Preço de Venda (+50%)[/bold cyan]", f"[bold cyan]R$ {indicadores['preco_venda']:,.2f}[/bold cyan]")
        table2.add_row("📊 Lucro Bruto", f"R$ {indicadores['lucro_bruto']:,.2f}")
        table2.add_row("📉 CSLL (9%)", f"[red]-R$ {indicadores['csll']:,.2f}[/red]")
        table2.add_row("[bold green]💰 Lucro Líquido Final[/bold green]", f"[bold green]R$ {indicadores['lucro_liquido_final']:,.2f}[/bold green]")
        
        console.print(table2)
        console.print()
        
        input("[yellow]Pressione ENTER para continuar...[/yellow]")
        console.clear()
    
    def modulo_4_rh(self):
        """Módulo 4: Recursos Humanos"""
        console.print(Panel.fit(
            "[bold magenta]👥 MÓDULO 4: RECURSOS HUMANOS[/bold magenta]",
            border_style="magenta"
        ))
        console.print()
        
        # Funcionários
        self.funcionarios = [
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
        
        data_manager.save_data('funcionarios.json', self.funcionarios)
        
        # Tabela de funcionários
        table = Table(title="✅ Quadro de Funcionários", box=box.ROUNDED)
        table.add_column("Matrícula", style="cyan", width=10)
        table.add_column("Nome", style="green", width=18)
        table.add_column("Cargo", style="yellow", width=25)
        table.add_column("R$/Hora", style="magenta", justify="right", width=10)
        table.add_column("Filhos", style="blue", justify="center", width=8)
        table.add_column("Salário Base", style="bold green", justify="right", width=15)
        
        total_folha = 0
        for func in self.funcionarios:
            salario_base = func['valor_hora'] * 220
            total_folha += salario_base
            table.add_row(
                func['matricula'],
                func['nome'],
                func['cargo'],
                f"R$ {func['valor_hora']:.2f}",
                str(func['qtd_filhos']),
                f"R$ {salario_base:,.2f}"
            )
        
        console.print(table)
        
        # Resumo
        console.print(f"\n[bold cyan]💼 Resumo da Folha de Pagamento:[/bold cyan]")
        console.print(f"  👥 Total de Funcionários: [bold]{len(self.funcionarios)}[/bold]")
        console.print(f"  💰 Folha Base Mensal (220h): [bold green]R$ {total_folha:,.2f}[/bold green]")
        
        # Distribuição por setor
        setores = {}
        for func in self.funcionarios:
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
        for setor, count in sorted(setores.items()):
            console.print(f"  • {setor}: [bold]{count}[/bold] funcionário(s)")
        
        console.print()
        input("[yellow]Pressione ENTER para ver o resumo final...[/yellow]")
        console.clear()
    
    def resumo_final(self):
        """Exibe o resumo final da apresentação"""
        console.print(Panel.fit(
            "[bold cyan]🎉 RESUMO FINAL - SISTEMA CARANGOS S/A[/bold cyan]",
            border_style="cyan"
        ))
        console.print()
        
        # Recalcular indicadores
        indicadores = financeiro.calcular_indicadores_financeiros()
        
        # Tabela de resumo
        table = Table(title="📊 Dashboard Executivo", box=box.DOUBLE_EDGE, show_header=True)
        table.add_column("Módulo", style="bold cyan", width=20)
        table.add_column("Indicador", style="yellow", width=30)
        table.add_column("Valor", style="bold green", justify="right", width=20)
        
        table.add_row("📦 ESTOQUE", "Produtos Cadastrados", f"{len(self.produtos)} itens")
        table.add_row("", "Investimento Total", f"R$ 1.980.500,00")
        table.add_row("", "", "")
        table.add_row("🏭 PRODUÇÃO", "Carros Produzidos (Semana)", f"{indicadores['total_produzido']} unidades")
        table.add_row("", "Eficiência", "261.9%")
        table.add_row("", "", "")
        table.add_row("💰 FINANCEIRO", "Custo Unitário", f"R$ {indicadores['custo_unitario']:,.2f}")
        table.add_row("", "Preço de Venda", f"R$ {indicadores['preco_venda']:,.2f}")
        table.add_row("", "Lucro Líquido", f"R$ {indicadores['lucro_liquido_final']:,.2f}")
        table.add_row("", "", "")
        table.add_row("👥 RH", "Funcionários Ativos", f"{len(self.funcionarios)} pessoas")
        table.add_row("", "Folha de Pagamento", "R$ 9.350,00")
        
        console.print(table)
        
        # Mensagem final
        console.print()
        console.print(Panel.fit(
            "[bold green]✅ SISTEMA OPERACIONAL E FUNCIONANDO PERFEITAMENTE![/bold green]\n\n"
            "[cyan]O Sistema Carangos S/A integra todos os módulos essenciais[/cyan]\n"
            "[cyan]para gestão completa de uma fábrica de automóveis:[/cyan]\n\n"
            "[white]✓ Controle de Estoque e Fornecedores[/white]\n"
            "[white]✓ Gestão de Produção e Metas[/white]\n"
            "[white]✓ Análise Financeira e Custos[/white]\n"
            "[white]✓ Recursos Humanos e Folha de Pagamento[/white]",
            title="🚗 Carangos S/A",
            border_style="green"
        ))
        console.print()
        console.print("[bold]Obrigado pela atenção! 🎓✨[/bold]\n")

def executar_apresentacao():
    """Executa a apresentação completa"""
    app = ApresentacaoCarangos()
    
    try:
        app.exibir_cabecalho()
        app.modulo_1_estoque()
        app.modulo_2_producao()
        app.modulo_3_financeiro()
        app.modulo_4_rh()
        app.resumo_final()
        
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️ Apresentação interrompida pelo usuário[/yellow]")
    except Exception as e:
        console.print(f"\n[red]❌ Erro durante a apresentação: {e}[/red]")
        import traceback
        console.print(traceback.format_exc())

if __name__ == "__main__":
    executar_apresentacao()
