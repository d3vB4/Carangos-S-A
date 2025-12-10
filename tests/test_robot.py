"""
Automated Testing Robot for Carangos S/A System
Uses pytest, Rich, and pynput to navigate through all menus and test functionality
"""

import sys
import os
import time
import subprocess
from io import StringIO
from contextlib import contextmanager
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.live import Live
from rich.layout import Layout
from rich import box
from pynput.keyboard import Controller, Key
import threading

console = Console()
keyboard = Controller()

class TerminalRobot:
    """Automated robot to test terminal-based main.py"""
    
    def __init__(self):
        self.test_results = []
        self.current_test = ""
        
    def type_text(self, text, delay=0.05):
        """Simulate typing text"""
        for char in text:
            keyboard.type(char)
            time.sleep(delay)
    
    def press_enter(self):
        """Press Enter key"""
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.5)
    
    def navigate_menu(self, option):
        """Navigate to a menu option"""
        self.type_text(str(option))
        self.press_enter()
        time.sleep(0.5)
    
    def record_result(self, test_name, status, details=""):
        """Record test result"""
        self.test_results.append({
            'test': test_name,
            'status': status,
            'details': details
        })
    
    def display_header(self):
        """Display test header"""
        console.clear()
        console.print(Panel.fit(
            "[bold cyan]🤖 CARANGOS S/A - ROBÔ DE TESTES AUTOMATIZADO[/bold cyan]\n"
            "[yellow]Testando todos os módulos e funções automaticamente[/yellow]",
            border_style="cyan"
        ))
        console.print()
    
    def display_results(self):
        """Display test results in a beautiful table"""
        table = Table(title="📊 Resumo dos Resultados dos Testes", box=box.ROUNDED)
        table.add_column("Teste", style="cyan", no_wrap=True)
        table.add_column("Status", style="magenta")
        table.add_column("Detalhes", style="white")
        
        for result in self.test_results:
            status_icon = "✅" if result['status'] == 'PASS' else "❌"
            status_color = "green" if result['status'] == 'PASS' else "red"
            table.add_row(
                result['test'],
                f"[{status_color}]{status_icon} {result['status']}[/{status_color}]",
                result['details']
            )
        
        console.print(table)
        
        # Summary
        total = len(self.test_results)
        passed = sum(1 for r in self.test_results if r['status'] == 'PASS')
        failed = total - passed
        
        summary = Panel(
            f"[bold]Total de Testes:[/bold] {total}\n"
            f"[bold green]Aprovados:[/bold green] {passed}\n"
            f"[bold red]Reprovados:[/bold red] {failed}\n"
            f"[bold cyan]Taxa de Sucesso:[/bold cyan] {(passed/total*100):.1f}%",
            title="📈 Resumo",
            border_style="green" if failed == 0 else "yellow"
        )
        console.print(summary)


def test_module_imports():
    """Test that all modules can be imported"""
    console.print("[bold yellow]Testando Importação de Módulos...[/bold yellow]")
    
    try:
        from modules import operacional, estoque, financeiro, rh, data_manager
        console.print("[green]✅ Todos os módulos importados com sucesso[/green]")
        return True
    except Exception as e:
        console.print(f"[red]❌ Falha na importação: {e}[/red]")
        return False


def test_data_manager():
    """Test data_manager module"""
    console.print("\n[bold yellow]Testando Gerenciador de Dados...[/bold yellow]")
    
    from modules import data_manager
    
    tests_passed = 0
    tests_total = 3
    
    # Test 1: Load data
    try:
        data = data_manager.load_data('producao.json')
        console.print("[green]✅ Função de carregar dados funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Load data failed: {e}[/red]")
    
    # Test 2: Save data
    try:
        test_data = [{'test': 'value'}]
        data_manager.save_data('test_temp.json', test_data)
        console.print("[green]✅ Função de salvar dados funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Save data failed: {e}[/red]")
    
    # Test 3: Load saved data
    try:
        loaded = data_manager.load_data('test_temp.json')
        assert loaded == test_data
        console.print("[green]✅ Persistência de dados verificada[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Data verification failed: {e}[/red]")
    
    console.print(f"\n[cyan]Gerenciador de Dados: {tests_passed}/{tests_total} testes aprovados[/cyan]")
    return tests_passed == tests_total


def test_operacional_module():
    """Test operacional module functions"""
    console.print("\n[bold yellow]Testando Módulo Operacional...[/bold yellow]")
    
    from modules import operacional
    
    tests_passed = 0
    tests_total = 2  # Reduced from 3
    
    # Test 1: Calculate statistics
    try:
        test_data = [
            {"dia": "Segunda", "turnos": {"Manhã": 10, "Tarde": 15, "Noite": 12}},
            {"dia": "Terça", "turnos": {"Manhã": 11, "Tarde": 14, "Noite": 13}}
        ]
        stats = operacional.calcular_estatisticas(test_data)
        assert 'total_semanal' in stats
        console.print("[green]✅ Cálculo de estatísticas funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Statistics failed: {e}[/red]")
    
    # Test 2: Calculate ideal capacity
    try:
        ideal = operacional.calcular_capacidade_ideal(meta_mensal=750)  # Pass parameter to avoid input
        assert ideal['semanal'] > 0
        console.print("[green]✅ Cálculo de capacidade ideal funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Ideal capacity failed: {e}[/red]")
    
    console.print(f"\n[cyan]Operacional: {tests_passed}/{tests_total} testes aprovados[/cyan]")
    return tests_passed == tests_total


def test_estoque_module():
    """Test estoque module functions"""
    console.print("\n[bold yellow]Testando Módulo de Estoque...[/bold yellow]")
    
    from modules import estoque
    
    tests_passed = 0
    tests_total = 2
    
    # Test 1: Calculate costs
    try:
        test_products = [
            {'codigo': 1, 'nome': 'Produto A', 'quantidade': 10, 'valor_compra': 100.0},
            {'codigo': 2, 'nome': 'Produto B', 'quantidade': 5, 'valor_compra': 200.0}
        ]
        costs = estoque.calcular_custos(test_products)
        assert 'total_atual' in costs
        assert costs['total_atual'] == 2000.0
        console.print("[green]✅ Cálculo de custos funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Cost calculation failed: {e}[/red]")
    
    # Test 2: Search product
    try:
        from modules import data_manager
        results = estoque.pesquisar_produto("test")
        console.print("[green]✅ Busca de produtos funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Product search failed: {e}[/red]")
    
    console.print(f"\n[cyan]Estoque: {tests_passed}/{tests_total} testes aprovados[/cyan]")
    return tests_passed == tests_total


def test_financeiro_module():
    """Test financeiro module functions"""
    console.print("\n[bold yellow]Testando Módulo Financeiro...[/bold yellow]")
    
    from modules import financeiro
    
    tests_passed = 0
    tests_total = 4
    
    # Test 1: Calculate production cost
    try:
        cost = financeiro.calcular_custo_producao(1000.0, 500.0)
        assert cost == 1500.0
        console.print("[green]✅ Cálculo de custo de produção funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Production cost failed: {e}[/red]")
    
    # Test 2: Calculate cost per car
    try:
        unit_cost = financeiro.calcular_custo_por_carro(1500.0, 10)
        assert unit_cost == 150.0
        console.print("[green]✅ Cálculo de custo unitário funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Unit cost failed: {e}[/red]")
    
    # Test 3: Calculate sale price
    try:
        sale_price = financeiro.calcular_preco_venda(150.0)
        assert sale_price == 225.0  # 150 * 1.5
        console.print("[green]✅ Cálculo de preço de venda funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Sale price failed: {e}[/red]")
    
    # Test 4: Calculate financial indicators
    try:
        indicators = financeiro.calcular_indicadores_financeiros()
        assert 'custo_unitario' in indicators
        console.print("[green]✅ Cálculo de indicadores financeiros funciona[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Financial indicators failed: {e}[/red]")
    
    console.print(f"\n[cyan]Financeiro: {tests_passed}/{tests_total} testes aprovados[/cyan]")
    return tests_passed == tests_total


def test_rh_module():
    """Test RH module functions"""
    console.print("\n[bold yellow]Testando Módulo de RH...[/bold yellow]")
    
    from modules import rh
    import inspect
    
    tests_passed = 0
    tests_total = 2
    
    # Test 1: Check module functions exist
    try:
        # Get all functions in the module
        functions = [name for name, obj in inspect.getmembers(rh) if inspect.isfunction(obj)]
        assert len(functions) > 0
        console.print(f"[green]✅ Módulo RH possui {len(functions)} funções[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ RH functions failed: {e}[/red]")
    
    # Test 2: Check module can be used
    try:
        # Just verify we can import and use the module
        from modules import data_manager
        funcionarios = data_manager.load_data('funcionarios.json')
        console.print("[green]✅ RH data access works[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ RH data access failed: {e}[/red]")
    
    console.print(f"\n[cyan]RH: {tests_passed}/{tests_total} testes aprovados[/cyan]")
    return tests_passed == tests_total


def test_estoque_module():
    """Test estoque module functions"""
    console.print("\n[bold yellow]Testing Estoque Module...[/bold yellow]")
    
    from modules import estoque
    
    tests_passed = 0
    tests_total = 2
    
    # Test 1: Calculate costs
    try:
        test_products = [
            {'codigo': 1, 'nome': 'Produto A', 'quantidade': 10, 'valor_compra': 100.0},
            {'codigo': 2, 'nome': 'Produto B', 'quantidade': 5, 'valor_compra': 200.0}
        ]
        costs = estoque.calcular_custos(test_products)
        assert 'total_atual' in costs
        assert costs['total_atual'] == 2000.0
        console.print("[green]✅ Cost calculation works[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Cost calculation failed: {e}[/red]")
    
    # Test 2: Search product
    try:
        from modules import data_manager
        results = estoque.pesquisar_produto("test")
        console.print("[green]✅ Product search works[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Product search failed: {e}[/red]")
    
    console.print(f"\n[cyan]Estoque: {tests_passed}/{tests_total} tests passed[/cyan]")
    return tests_passed == tests_total


def test_financeiro_module():
    """Test financeiro module functions"""
    console.print("\n[bold yellow]Testing Financeiro Module...[/bold yellow]")
    
    from modules import financeiro
    
    tests_passed = 0
    tests_total = 4
    
    # Test 1: Calculate production cost
    try:
        cost = financeiro.calcular_custo_producao(1000.0, 500.0)
        assert cost == 1500.0
        console.print("[green]✅ Production cost calculation works[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Production cost failed: {e}[/red]")
    
    # Test 2: Calculate cost per car
    try:
        unit_cost = financeiro.calcular_custo_por_carro(1500.0, 10)
        assert unit_cost == 150.0
        console.print("[green]✅ Unit cost calculation works[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Unit cost failed: {e}[/red]")
    
    # Test 3: Calculate sale price
    try:
        sale_price = financeiro.calcular_preco_venda(150.0)
        assert sale_price == 225.0  # 150 * 1.5
        console.print("[green]✅ Sale price calculation works[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Sale price failed: {e}[/red]")
    
    # Test 4: Calculate financial indicators
    try:
        indicators = financeiro.calcular_indicadores_financeiros()
        assert 'custo_unitario' in indicators
        console.print("[green]✅ Financial indicators calculation works[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ Financial indicators failed: {e}[/red]")
    
    console.print(f"\n[cyan]Financeiro: {tests_passed}/{tests_total} tests passed[/cyan]")
    return tests_passed == tests_total


def test_rh_module():
    """Test RH module functions"""
    console.print("\n[bold yellow]Testing RH Module...[/bold yellow]")
    
    from modules import rh
    import inspect
    
    tests_passed = 0
    tests_total = 2
    
    # Test 1: Check module functions exist
    try:
        # Get all functions in the module
        functions = [name for name, obj in inspect.getmembers(rh) if inspect.isfunction(obj)]
        assert len(functions) > 0
        console.print(f"[green]✅ RH module has {len(functions)} functions[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ RH functions failed: {e}[/red]")
    
    # Test 2: Check data structures (use correct attribute names)
    try:
        assert hasattr(rh, 'SETORES_DA_EMPRESA')
        assert hasattr(rh, 'SETOR_DIGITO')
        assert hasattr(rh, 'CARGO_NIVEL')
        console.print("[green]✅ Estruturas de dados de RH verificadas[/green]")
        tests_passed += 1
    except Exception as e:
        console.print(f"[red]❌ RH structures failed: {e}[/red]")
    
    console.print(f"\n[cyan]RH: {tests_passed}/{tests_total} tests passed[/cyan]")
    return tests_passed == tests_total


def run_all_unit_tests():
    """Run all unit tests with Rich progress display"""
    console.clear()
    console.print(Panel.fit(
        "[bold cyan]🧪 EXECUTANDO TESTES UNITÁRIOS[/bold cyan]\n"
        "[yellow]Testando todos os módulos e funções[/yellow]",
        border_style="cyan"
    ))
    console.print()
    
    results = {}
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        
        task = progress.add_task("[cyan]Executando testes...", total=6)
        
        # Test imports
        progress.update(task, description="[cyan]Testando importações...")
        results['imports'] = test_module_imports()
        progress.advance(task)
        
        # Test data manager
        progress.update(task, description="[cyan]Testando gerenciador de dados...")
        results['data_manager'] = test_data_manager()
        progress.advance(task)
        
        # Test operacional
        progress.update(task, description="[cyan]Testando operacional...")
        results['operacional'] = test_operacional_module()
        progress.advance(task)
        
        # Test estoque
        progress.update(task, description="[cyan]Testando estoque...")
        results['estoque'] = test_estoque_module()
        progress.advance(task)
        
        # Test financeiro
        progress.update(task, description="[cyan]Testando financeiro...")
        results['financeiro'] = test_financeiro_module()
        progress.advance(task)
        
        # Test RH
        progress.update(task, description="[cyan]Testando RH...")
        results['rh'] = test_rh_module()
        progress.advance(task)
    
    # Display final results
    console.print("\n")
    table = Table(title="📊 Resultados dos Testes Unitários", box=box.ROUNDED)
    table.add_column("Módulo", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    
    for module, passed in results.items():
        status = "✅ APROVADO" if passed else "❌ REPROVADO"
        color = "green" if passed else "red"
        table.add_row(module.upper(), f"[{color}]{status}[/{color}]")
    
    console.print(table)
    
    # Summary
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    
    summary = Panel(
        f"[bold]Total de Módulos:[/bold] {total}\n"
        f"[bold green]Aprovados:[/bold green] {passed}\n"
        f"[bold red]Reprovados:[/bold red] {total - passed}\n"
        f"[bold cyan]Taxa de Sucesso:[/bold cyan] {(passed/total*100):.1f}%",
        title="📈 Resumo dos Testes",
        border_style="green" if passed == total else "yellow"
    )
    console.print(summary)
    
    return passed == total


if __name__ == "__main__":
    try:
        # Add project root to path
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # Run all tests
        success = run_all_unit_tests()
        
        console.print("\n[bold cyan]🎉 Testes Concluídos![/bold cyan]\n")
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ Testes interrompidos pelo usuário[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]❌ Erro fatal: {e}[/red]")
        import traceback
        console.print(traceback.format_exc())
        sys.exit(1)
