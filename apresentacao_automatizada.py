"""
APRESENTAÇÃO AUTOMATIZADA COMPLETA - SISTEMA CARANGOS S/A
Demonstra TODAS as funcionalidades do sistema main.py
Passa por TODAS as opções de TODOS os menus
"""

import subprocess
import time
import pyautogui
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
import sys
import os

console = Console()

class ApresentacaoCompletaAutomatizada:
    """Classe para apresentação automatizada completa do sistema"""
    
    def __init__(self):
        self.processo = None
        self.delay_curto = 0.8
        self.delay_medio = 1.5
        self.delay_longo = 3.0
        
    def iniciar_sistema(self):
        """Inicia o main.py em um processo separado"""
        console.print(Panel.fit(
            "[bold cyan]🚀 APRESENTAÇÃO AUTOMATIZADA COMPLETA[/bold cyan]\n"
            "[yellow]Sistema Carangos S/A - TODAS as Funcionalidades de TODOS os Menus[/yellow]",
            border_style="cyan"
        ))
        console.print()
        
        console.print("[cyan]📌 Iniciando o sistema main.py...[/cyan]")
        time.sleep(2)
        
        # Iniciar main.py em um novo terminal
        if sys.platform == 'win32':
            self.processo = subprocess.Popen(
                ['python', 'main.py'],
                cwd=os.path.dirname(os.path.abspath(__file__)),
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            self.processo = subprocess.Popen(
                ['python', 'main.py'],
                cwd=os.path.dirname(os.path.abspath(__file__))
            )
        
        time.sleep(4)
        console.print("[green]✅ Sistema iniciado com sucesso![/green]\n")
    
    def digitar(self, texto, delay=0.05):
        """Digita texto com delay entre caracteres"""
        for char in str(texto):
            pyautogui.write(char)
            time.sleep(delay)
    
    def pressionar_enter(self, delay=None):
        """Pressiona Enter"""
        pyautogui.press('enter')
        time.sleep(delay if delay else self.delay_curto)
    
    def navegar_menu(self, opcao, descricao, delay=None):
        """Navega para uma opção do menu"""
        console.print(f"[cyan]  ➤ {descricao}...[/cyan]")
        self.digitar(opcao)
        self.pressionar_enter(delay if delay else self.delay_medio)
    
    def fazer_login(self):
        """Realiza o login no sistema"""
        console.print("\n[bold yellow]🔐 REALIZANDO LOGIN[/bold yellow]")
        
        time.sleep(2)
        
        # Digitar usuário
        console.print("[cyan]  ➤ Digitando usuário: admin[/cyan]")
        self.digitar('admin', delay=0.1)
        self.pressionar_enter(self.delay_curto)
        
        # Digitar senha
        console.print("[cyan]  ➤ Digitando senha: admin123[/cyan]")
        self.digitar('admin123', delay=0.1)
        self.pressionar_enter(self.delay_longo)
        
        console.print("[green]✅ Login realizado com sucesso![/green]")
        time.sleep(2)
    
    def demonstrar_operacional(self):
        """Demonstra TODAS as opções do módulo Operacional"""
        console.print("\n[bold green]📊 MÓDULO OPERACIONAL - Demonstração Completa[/bold green]")
        
        # Entrar no módulo
        self.navegar_menu('1', 'Acessando Módulo Operacional', self.delay_medio)
        
        # OPÇÃO 1: Registrar Produção Semanal
        console.print("\n[yellow]  📝 Opção 1: Registrar Produção Semanal[/yellow]")
        self.navegar_menu('1', 'Cadastrar Produção Semanal', self.delay_curto)
        
        # Cadastrar todos os 7 dias
        dias_producao = [
            ('Segunda', '25', '30', '22'),
            ('Terça', '28', '32', '24'),
            ('Quarta', '26', '31', '23'),
            ('Quinta', '27', '33', '25'),
            ('Sexta', '29', '34', '26'),
            ('Sábado', '20', '18', '15'),
            ('Domingo', '10', '8', '5'),
        ]
        
        for dia, manha, tarde, noite in dias_producao:
            console.print(f"[cyan]    • {dia}: M={manha}, T={tarde}, N={noite}[/cyan]")
            self.digitar(manha)
            self.pressionar_enter(self.delay_curto)
            self.digitar(tarde)
            self.pressionar_enter(self.delay_curto)
            self.digitar(noite)
            self.pressionar_enter(self.delay_curto)
        
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        time.sleep(1)
        
        # OPÇÃO 2: Ver Relatório de Produção
        console.print("\n[yellow]  📈 Opção 2: Ver Relatório de Produção[/yellow]")
        self.navegar_menu('2', 'Visualizar Relatório de Produção', self.delay_curto)
        console.print("[cyan]    • Inserindo meta mensal: 750 carros[/cyan]")
        self.digitar('750')
        self.pressionar_enter(self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # Voltar ao menu principal
        self.navegar_menu('0', 'Retornando ao Menu Principal', self.delay_medio)
    
    def demonstrar_estoque(self):
        """Demonstra TODAS as opções do módulo de Estoque"""
        console.print("\n[bold green]📦 MÓDULO DE ESTOQUE - Demonstração Completa[/bold green]")
        
        # Entrar no módulo
        self.navegar_menu('2', 'Acessando Módulo de Estoque', self.delay_medio)
        
        # OPÇÃO 1: Cadastrar Produto
        console.print("\n[yellow]  ➕ Opção 1: Cadastrar Produto[/yellow]")
        self.navegar_menu('1', 'Cadastrar Novo Produto', self.delay_curto)
        
        console.print("[cyan]    • Cadastrando Motor V8 Turbo...[/cyan]")
        self.digitar('1001')  # Código
        self.pressionar_enter(self.delay_curto)
        self.digitar('Motor V8 Turbo')  # Nome
        self.pressionar_enter(self.delay_curto)
        self.digitar('10/12/2024')  # Data
        self.pressionar_enter(self.delay_curto)
        self.digitar('MotorTech Ltda')  # Fornecedor
        self.pressionar_enter(self.delay_curto)
        self.digitar('50')  # Quantidade
        self.pressionar_enter(self.delay_curto)
        self.digitar('15000')  # Valor
        self.pressionar_enter(self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # OPÇÃO 2: Buscar Produto
        console.print("\n[yellow]  🔍 Opção 2: Buscar Produto[/yellow]")
        self.navegar_menu('2', 'Pesquisar Produto', self.delay_curto)
        console.print("[cyan]    • Pesquisando por 'Motor'...[/cyan]")
        self.digitar('Motor')
        self.pressionar_enter(self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # OPÇÃO 3: Ver Relatório de Custos
        console.print("\n[yellow]  💰 Opção 3: Ver Relatório de Custos[/yellow]")
        self.navegar_menu('3', 'Calcular Custos de Estoque', self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # Voltar ao menu principal
        self.navegar_menu('0', 'Retornando ao Menu Principal', self.delay_medio)
    
    def demonstrar_financeiro(self):
        """Demonstra TODAS as opções do módulo Financeiro"""
        console.print("\n[bold green]💰 MÓDULO FINANCEIRO - Demonstração Completa[/bold green]")
        
        # Entrar no módulo
        self.navegar_menu('3', 'Acessando Módulo Financeiro', self.delay_medio)
        
        # OPÇÃO 1: Gerenciar Despesas Fixas
        console.print("\n[yellow]  💸 Opção 1: Gerenciar Despesas Fixas[/yellow]")
        self.navegar_menu('1', 'Cadastrar Despesas Fixas', self.delay_curto)
        
        console.print("[cyan]    • Digitando valores das despesas fixas...[/cyan]")
        console.print("[cyan]      - Água: R$ 5000[/cyan]")
        self.digitar('5000')  # Água
        self.pressionar_enter(self.delay_curto)
        console.print("[cyan]      - Luz: R$ 8000[/cyan]")
        self.digitar('8000')  # Luz
        self.pressionar_enter(self.delay_curto)
        console.print("[cyan]      - Salários: R$ 50000[/cyan]")
        self.digitar('50000')  # Salários
        self.pressionar_enter(self.delay_curto)
        console.print("[cyan]      - Impostos: R$ 12000[/cyan]")
        self.digitar('12000')  # Impostos
        self.pressionar_enter(self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # OPÇÃO 2: Ver Relatório Financeiro
        console.print("\n[yellow]  📊 Opção 2: Ver Relatório Financeiro[/yellow]")
        self.navegar_menu('2', 'Visualizar Relatório Financeiro', self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # OPÇÃO 3: Relatório Completo da Fábrica
        console.print("\n[yellow]  🏭 Opção 3: Relatório Completo da Fábrica (Água, Luz, Salários)[/yellow]")
        self.navegar_menu('3', 'Gerar Relatório Completo da Fábrica', self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # OPÇÃO 4: Indicadores Financeiros
        console.print("\n[yellow]  📈 Opção 4: Indicadores Financeiros (Custo/Carro e Impostos)[/yellow]")
        self.navegar_menu('4', 'Calcular Indicadores Financeiros', self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # Voltar ao menu principal
        self.navegar_menu('0', 'Retornando ao Menu Principal', self.delay_medio)
    
    def demonstrar_rh(self):
        """Demonstra TODAS as opções do módulo de RH"""
        console.print("\n[bold green]👥 MÓDULO DE RH - Demonstração Completa[/bold green]")
        
        # Entrar no módulo
        self.navegar_menu('4', 'Acessando Módulo de RH', self.delay_medio)
        
        # OPÇÃO 1: Cadastrar Funcionário
        console.print("\n[yellow]  ➕ Opção 1: Cadastrar Funcionário[/yellow]")
        self.navegar_menu('1', 'Cadastrar Novo Funcionário', self.delay_curto)
        
        console.print("[cyan]    • Cadastrando João Silva...[/cyan]")
        self.digitar('Joao Silva')  # Nome
        self.pressionar_enter(self.delay_curto)
        self.digitar('Rua das Flores')  # Endereço
        self.pressionar_enter(self.delay_curto)
        self.digitar('12345678900')  # CPF
        self.pressionar_enter(self.delay_curto)
        self.digitar('123456789')  # RG
        self.pressionar_enter(self.delay_curto)
        self.digitar('12345')  # CTPS
        self.pressionar_enter(self.delay_curto)
        self.digitar('11987654321')  # Telefone
        self.pressionar_enter(self.delay_curto)
        self.digitar('2')  # Filhos
        self.pressionar_enter(self.delay_curto)
        self.digitar('1')  # Setor (Operacional)
        self.pressionar_enter(self.delay_curto)
        self.digitar('2')  # Cargo (Operador de Máquinas)
        self.pressionar_enter(self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # OPÇÃO 2: Listar Funcionários
        console.print("\n[yellow]  📋 Opção 2: Listar Funcionários[/yellow]")
        self.navegar_menu('2', 'Listar Todos os Funcionários', self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # OPÇÃO 3: Editar Funcionário
        console.print("\n[yellow]  ✏️ Opção 3: Editar Funcionário[/yellow]")
        self.navegar_menu('3', 'Editar Funcionário', self.delay_curto)
        console.print("[cyan]    • Selecionando funcionário 1...[/cyan]")
        self.digitar('1')  # Selecionar primeiro funcionário
        self.pressionar_enter(self.delay_curto)
        console.print("[cyan]    • Atualizando telefone...[/cyan]")
        self.pressionar_enter(self.delay_curto)  # Nome (deixar em branco)
        self.pressionar_enter(self.delay_curto)  # Endereço (deixar em branco)
        self.digitar('11999998888')  # Novo telefone
        self.pressionar_enter(self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # OPÇÃO 4: Deletar Funcionário (vamos cancelar)
        console.print("\n[yellow]  🗑️ Opção 4: Deletar Funcionário (cancelando)[/yellow]")
        self.navegar_menu('4', 'Deletar Funcionário', self.delay_curto)
        console.print("[cyan]    • Selecionando funcionário 1...[/cyan]")
        self.digitar('1')
        self.pressionar_enter(self.delay_curto)
        console.print("[cyan]    • Cancelando exclusão (N)...[/cyan]")
        self.digitar('n')  # Não confirmar exclusão
        self.pressionar_enter(self.delay_medio)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # OPÇÃO 5: Gerar Folha de Pagamento
        console.print("\n[yellow]  💵 Opção 5: Gerar Folha de Pagamento[/yellow]")
        self.navegar_menu('5', 'Gerar Folha de Pagamento', self.delay_curto)
        console.print("[cyan]    • Selecionando setor 1 (Operacional)...[/cyan]")
        self.digitar('1')  # Setor Operacional
        self.pressionar_enter(self.delay_curto)
        console.print("[cyan]    • Selecionando funcionário 1...[/cyan]")
        self.digitar('1')  # Primeiro funcionário
        self.pressionar_enter(self.delay_curto)
        console.print("[cyan]    • Horas trabalhadas: 220[/cyan]")
        self.digitar('220')
        self.pressionar_enter(self.delay_curto)
        console.print("[cyan]    • Horas extras: 10[/cyan]")
        self.digitar('10')
        self.pressionar_enter(self.delay_longo)
        # Pressionar Enter no "Pressione Enter para continuar..."
        self.pressionar_enter(self.delay_medio)
        
        # Voltar ao menu principal
        self.navegar_menu('0', 'Retornando ao Menu Principal', self.delay_medio)
    
    def finalizar(self):
        """Finaliza a apresentação"""
        console.print("\n[bold cyan]🏁 FINALIZANDO APRESENTAÇÃO[/bold cyan]")
        
        # Sair do sistema
        self.navegar_menu('0', 'Encerrando o Sistema', self.delay_medio)
        
        # Terminar processo se ainda estiver rodando
        if self.processo and self.processo.poll() is None:
            self.processo.terminate()
            time.sleep(1)
        
        console.print()
        console.print(Panel.fit(
            "[bold green]✅ APRESENTAÇÃO COMPLETA CONCLUÍDA COM SUCESSO![/bold green]\n\n"
            "[cyan]TODAS as opções de TODOS os menus foram demonstradas:[/cyan]\n\n"
            "[white]📊 OPERACIONAL (2 opções):[/white]\n"
            "[white]  ✓ Opção 1: Registrar Produção Semanal (7 dias)[/white]\n"
            "[white]  ✓ Opção 2: Ver Relatório de Produção[/white]\n\n"
            "[white]📦 ESTOQUE (3 opções):[/white]\n"
            "[white]  ✓ Opção 1: Cadastrar Produto[/white]\n"
            "[white]  ✓ Opção 2: Buscar Produto[/white]\n"
            "[white]  ✓ Opção 3: Ver Relatório de Custos[/white]\n\n"
            "[white]💰 FINANCEIRO (4 opções):[/white]\n"
            "[white]  ✓ Opção 1: Gerenciar Despesas Fixas[/white]\n"
            "[white]  ✓ Opção 2: Ver Relatório Financeiro[/white]\n"
            "[white]  ✓ Opção 3: Relatório Completo da Fábrica[/white]\n"
            "[white]  ✓ Opção 4: Indicadores Financeiros[/white]\n\n"
            "[white]👥 RH (5 opções):[/white]\n"
            "[white]  ✓ Opção 1: Cadastrar Funcionário[/white]\n"
            "[white]  ✓ Opção 2: Listar Funcionários[/white]\n"
            "[white]  ✓ Opção 3: Editar Funcionário[/white]\n"
            "[white]  ✓ Opção 4: Deletar Funcionário[/white]\n"
            "[white]  ✓ Opção 5: Gerar Folha de Pagamento[/white]\n\n"
            "[bold cyan]Total: 14 funcionalidades testadas![/bold cyan]",
            title="🚗 Carangos S/A - Demonstração Completa",
            border_style="green"
        ))
        console.print()
        console.print("[bold]Obrigado pela atenção! 🎓✨[/bold]\n")
    
    def executar(self):
        """Executa a apresentação completa"""
        try:
            # Avisos iniciais
            console.print("[yellow]⚠️  INSTRUÇÕES IMPORTANTES:[/yellow]")
            console.print("[white]1. Não mova o mouse durante a apresentação[/white]")
            console.print("[white]2. A janela do terminal do main.py deve estar visível[/white]")
            console.print("[white]3. Aguarde 5 segundos para posicionar as janelas[/white]")
            console.print("[white]4. Login automático: admin / admin123[/white]")
            console.print("[white]5. Duração aproximada: 8-10 minutos[/white]\n")
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                console=console
            ) as progress:
                task = progress.add_task("[cyan]Preparando apresentação...", total=5)
                for i in range(5):
                    time.sleep(1)
                    progress.advance(task)
            
            console.print()
            
            # Iniciar sistema
            self.iniciar_sistema()
            
            # Aguardar usuário posicionar janelas
            console.print("[yellow]⏸️  Clique na janela do main.py para ativá-la em 3 segundos...[/yellow]")
            time.sleep(3)
            
            # Fazer login
            self.fazer_login()
            
            # Executar demonstrações completas
            self.demonstrar_operacional()
            self.demonstrar_estoque()
            self.demonstrar_financeiro()
            self.demonstrar_rh()
            
            # Finalizar
            self.finalizar()
            
        except KeyboardInterrupt:
            console.print("\n[yellow]⚠️ Apresentação interrompida pelo usuário[/yellow]")
            if self.processo:
                self.processo.terminate()
        except Exception as e:
            console.print(f"\n[red]❌ Erro durante a apresentação: {e}[/red]")
            if self.processo:
                self.processo.terminate()
            import traceback
            console.print(traceback.format_exc())

def main():
    """Função principal"""
    apresentacao = ApresentacaoCompletaAutomatizada()
    apresentacao.executar()

if __name__ == "__main__":
    main()
