"""
Live Demo Script for Carangos S/A System
Demonstrates complete workflows through all modules
"""

import sys
import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import operacional, estoque, financeiro, rh, data_manager

console = Console()


class LiveDemo:
    """Live demonstration of the Carangos S/A system"""
    
    def __init__(self):
        self.demo_data = {}
    
    def show_header(self, title):
        """Display section header"""
        console.clear()
        console.print(Panel.fit(
            f"[bold cyan]{title}[/bold cyan]",
            border_style="cyan"
        ))
        console.print()
    
    def pause(self, message="Press Enter to continue..."):
        """Pause for user input"""
        console.print(f"\n[dim]{message}[/dim]")
        input()
    
    def demo_operacional(self):
        """Demonstrate Operacional module"""
        self.show_header("🏭 MÓDULO OPERACIONAL - Controle de Produção")
        
        console.print("[yellow]Demonstrating production tracking...[/yellow]\n")
        
        # Load production data
        producao = data_manager.load_data('producao.json')
        
        if producao:
            # Reconstruct structure
            dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
            dados_estruturados = []
            
            for dia in dias_semana:
                turnos_dia = {"Manhã": 0, "Tarde": 0, "Noite": 0}
                rows = [row for row in producao if row['dia'] == dia]
                for row in rows:
                    if row['turno'] in turnos_dia:
                        turnos_dia[row['turno']] += row['quantidade']
                dados_estruturados.append({"dia": dia, "turnos": turnos_dia})
            
            # Calculate statistics
            stats = operacional.calcular_estatisticas(dados_estruturados)
            ideal = operacional.calcular_capacidade_ideal()
            
            # Display production table
            table = Table(title="📊 Produção Semanal", box=box.ROUNDED)
            table.add_column("Dia", style="cyan")
            table.add_column("Manhã", style="green")
            table.add_column("Tarde", style="yellow")
            table.add_column("Noite", style="blue")
            table.add_column("Total", style="magenta", justify="right")
            
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
            
            # Display statistics
            console.print(f"\n[bold cyan]Estatísticas:[/bold cyan]")
            console.print(f"  Total Semanal: [bold]{stats['total_semanal']}[/bold] carros")
            console.print(f"  Média Diária: [bold]{stats['media_diaria']:.1f}[/bold] carros")
            console.print(f"  Capacidade Ideal: [bold]{ideal}[/bold] carros")
            console.print(f"  Eficiência: [bold]{stats['eficiencia']:.1f}%[/bold]")
        else:
            console.print("[yellow]⚠ No production data available[/yellow]")
        
        self.pause()
    
    def demo_estoque(self):
        """Demonstrate Estoque module"""
        self.show_header("📦 MÓDULO DE ESTOQUE - Gestão de Insumos")
        
        console.print("[yellow]Demonstrating inventory management...[/yellow]\n")
        
        # Load products
        produtos = data_manager.load_data('produtos.json')
        
        if produtos:
            # Display products table
            table = Table(title="📋 Produtos em Estoque", box=box.ROUNDED)
            table.add_column("Código", style="cyan")
            table.add_column("Nome", style="green")
            table.add_column("Fornecedor", style="yellow")
            table.add_column("Quantidade", style="magenta", justify="right")
            table.add_column("Valor Unit.", style="blue", justify="right")
            table.add_column("Total", style="bold green", justify="right")
            
            for p in produtos[:10]:  # Show first 10
                total = p['quantidade'] * p['valor_compra']
                table.add_row(
                    str(p['codigo']),
                    p['nome'],
                    p['fornecedor'],
                    str(p['quantidade']),
                    f"R$ {p['valor_compra']:.2f}",
                    f"R$ {total:.2f}"
                )
            
            console.print(table)
            
            # Calculate costs
            custos = estoque.calcular_custos(produtos)
            
            console.print(f"\n[bold cyan]Análise de Custos:[/bold cyan]")
            console.print(f"  Custo Total Atual: [bold green]R$ {custos['total_atual']:,.2f}[/bold green]")
            console.print(f"  Projeção Mensal: [bold yellow]R$ {custos['mensal_projetado']:,.2f}[/bold yellow]")
            console.print(f"  Projeção Anual: [bold blue]R$ {custos['anual_projetado']:,.2f}[/bold blue]")
        else:
            console.print("[yellow]⚠ No products in inventory[/yellow]")
        
        self.pause()
    
    def demo_financeiro(self):
        """Demonstrate Financeiro module"""
        self.show_header("💰 MÓDULO FINANCEIRO - Análise Financeira")
        
        console.print("[yellow]Demonstrating financial analysis...[/yellow]\n")
        
        # Calculate financial indicators
        indicadores = financeiro.calcular_indicadores_financeiros()
        
        # Display indicators table
        table = Table(title="📊 Indicadores Financeiros", box=box.ROUNDED)
        table.add_column("Indicador", style="cyan")
        table.add_column("Valor", style="green", justify="right")
        
        table.add_row("Produção Total", f"{indicadores['total_produzido']} carros")
        table.add_row("Custo Fixo Total", f"R$ {indicadores['custo_fixo_total']:,.2f}")
        table.add_row("Custo Estoque", f"R$ {indicadores['custo_estoque_total']:,.2f}")
        table.add_row("[bold]Custo Unitário[/bold]", f"[bold]R$ {indicadores['custo_unitario']:,.2f}[/bold]")
        table.add_row("[bold cyan]Preço de Venda (+50%)[/bold cyan]", f"[bold cyan]R$ {indicadores['preco_venda']:,.2f}[/bold cyan]")
        table.add_row("Lucro Bruto", f"R$ {indicadores['lucro_bruto']:,.2f}")
        table.add_row("CSLL (9%)", f"[red]-R$ {indicadores['csll']:,.2f}[/red]")
        table.add_row("[bold green]Lucro Líquido[/bold green]", f"[bold green]R$ {indicadores['lucro_liquido_final']:,.2f}[/bold green]")
        
        console.print(table)
        
        # Calculate margins
        margem_bruta = (indicadores['lucro_bruto'] / (indicadores['preco_venda'] * indicadores['total_produzido'])) * 100 if indicadores['total_produzido'] > 0 else 0
        margem_liquida = (indicadores['lucro_liquido_final'] / (indicadores['preco_venda'] * indicadores['total_produzido'])) * 100 if indicadores['total_produzido'] > 0 else 0
        
        console.print(f"\n[bold cyan]Margens:[/bold cyan]")
        console.print(f"  Margem Bruta: [bold]{margem_bruta:.1f}%[/bold]")
        console.print(f"  Margem Líquida: [bold green]{margem_liquida:.1f}%[/bold green]")
        
        self.pause()
    
    def demo_rh(self):
        """Demonstrate RH module"""
        self.show_header("👥 MÓDULO DE RH - Gestão de Pessoas")
        
        console.print("[yellow]Demonstrating HR management...[/yellow]\n")
        
        # Load employees
        funcionarios = data_manager.load_data('funcionarios.json')
        
        if funcionarios:
            # Display employees table
            table = Table(title="👔 Funcionários Cadastrados", box=box.ROUNDED)
            table.add_column("Nome", style="cyan")
            table.add_column("Setor", style="green")
            table.add_column("Cargo", style="yellow")
            table.add_column("Salário Base", style="magenta", justify="right")
            
            total_folha = 0
            for func in funcionarios[:10]:  # Show first 10
                table.add_row(
                    func['nome'],
                    func['setor'],
                    func['cargo'],
                    f"R$ {func['salario_base']:,.2f}"
                )
                total_folha += func['salario_base']
            
            console.print(table)
            
            console.print(f"\n[bold cyan]Resumo da Folha:[/bold cyan]")
            console.print(f"  Total de Funcionários: [bold]{len(funcionarios)}[/bold]")
            console.print(f"  Folha de Pagamento (Base): [bold green]R$ {total_folha:,.2f}[/bold green]")
            
            # Count by sector
            setores = {}
            for func in funcionarios:
                setor = func['setor']
                setores[setor] = setores.get(setor, 0) + 1
            
            console.print(f"\n[bold cyan]Distribuição por Setor:[/bold cyan]")
            for setor, count in setores.items():
                console.print(f"  {setor}: [bold]{count}[/bold] funcionários")
        else:
            console.print("[yellow]⚠ No employees registered[/yellow]")
        
        self.pause()
    
    def run_full_demo(self):
        """Run complete demonstration"""
        console.clear()
        console.print(Panel.fit(
            "[bold cyan]🎬 CARANGOS S/A - LIVE DEMONSTRATION[/bold cyan]\n"
            "[yellow]Complete system walkthrough[/yellow]",
            border_style="cyan"
        ))
        console.print()
        
        console.print("[bold]This demo will showcase all modules:[/bold]")
        console.print("  1. 🏭 Operacional - Production tracking")
        console.print("  2. 📦 Estoque - Inventory management")
        console.print("  3. 💰 Financeiro - Financial analysis")
        console.print("  4. 👥 RH - Human resources")
        console.print()
        
        if not Confirm.ask("Ready to start?", default=True):
            return
        
        # Run demos
        self.demo_operacional()
        self.demo_estoque()
        self.demo_financeiro()
        self.demo_rh()
        
        # Final summary
        self.show_header("✅ DEMONSTRATION COMPLETE")
        console.print("[bold green]All modules demonstrated successfully![/bold green]\n")
        console.print("[cyan]The Carangos S/A system provides:[/cyan]")
        console.print("  ✓ Complete production tracking")
        console.print("  ✓ Inventory and cost management")
        console.print("  ✓ Financial analysis and reporting")
        console.print("  ✓ HR and payroll management")
        console.print()
        console.print("[bold]Thank you for watching! 🎉[/bold]")


if __name__ == "__main__":
    try:
        demo = LiveDemo()
        demo.run_full_demo()
    except KeyboardInterrupt:
        console.print("\n[yellow]Demo interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        import traceback
        console.print(traceback.format_exc())
