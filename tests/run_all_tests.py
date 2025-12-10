"""
Master Test Runner for Carangos S/A System
Runs all tests and generates comprehensive reports
"""

import sys
import os
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich import box
from datetime import datetime

console = Console()


def run_command(cmd, description):
    """Run a command and return success status"""
    console.print(f"\n[cyan]Running: {description}[/cyan]")
    console.print(f"[dim]Command: {cmd}[/dim]\n")
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        
        if result.returncode == 0:
            console.print(f"[green]✅ {description} - PASSED[/green]")
            return True, result.stdout
        else:
            console.print(f"[red]❌ {description} - FAILED[/red]")
            if result.stderr:
                console.print(f"[red]{result.stderr}[/red]")
            return False, result.stderr
    except Exception as e:
        console.print(f"[red]❌ Error running {description}: {e}[/red]")
        return False, str(e)


def main():
    """Run all tests"""
    console.clear()
    console.print(Panel.fit(
        "[bold cyan]🧪 CARANGOS S/A - MASTER TEST RUNNER[/bold cyan]\n"
        "[yellow]Running comprehensive test suite[/yellow]",
        border_style="cyan"
    ))
    console.print()
    
    start_time = time.time()
    results = {}
    
    # Test suite
    tests = [
        {
            'name': 'Unit Tests (Robot)',
            'cmd': 'python tests/test_robot.py',
            'description': 'Automated unit tests for all modules'
        },
        {
            'name': 'Integration Tests',
            'cmd': 'python -m pytest tests/test_modules.py -v',
            'description': 'Module integration tests'
        },
        {
            'name': 'Operacional Tests',
            'cmd': 'python -m pytest tests/test_operacional.py -v',
            'description': 'Operacional module specific tests'
        },
        {
            'name': 'Terminal Flow Tests',
            'cmd': 'python -m pytest tests/test_terminal_flow.py -v',
            'description': 'Terminal navigation flow tests'
        },
        {
            'name': 'Web Integration Tests',
            'cmd': 'python -m pytest tests/test_web_integration.py -v',
            'description': 'Web interface integration tests'
        }
    ]
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        
        task = progress.add_task("[cyan]Running test suite...", total=len(tests))
        
        for test in tests:
            progress.update(task, description=f"[cyan]{test['name']}...")
            success, output = run_command(test['cmd'], test['description'])
            results[test['name']] = {
                'success': success,
                'output': output
            }
            progress.advance(task)
            time.sleep(0.5)
    
    # Display results
    console.print("\n")
    console.print("=" * 80)
    console.print()
    
    table = Table(title="📊 Test Results Summary", box=box.ROUNDED)
    table.add_column("Test Suite", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Details", style="white")
    
    for test_name, result in results.items():
        status = "✅ PASS" if result['success'] else "❌ FAIL"
        color = "green" if result['success'] else "red"
        details = "All tests passed" if result['success'] else "Some tests failed"
        table.add_row(
            test_name,
            f"[{color}]{status}[/{color}]",
            details
        )
    
    console.print(table)
    
    # Summary
    total = len(results)
    passed = sum(1 for r in results.values() if r['success'])
    failed = total - passed
    elapsed = time.time() - start_time
    
    summary = Panel(
        f"[bold]Total Test Suites:[/bold] {total}\n"
        f"[bold green]Passed:[/bold green] {passed}\n"
        f"[bold red]Failed:[/bold red] {failed}\n"
        f"[bold cyan]Success Rate:[/bold cyan] {(passed/total*100):.1f}%\n"
        f"[bold yellow]Time Elapsed:[/bold yellow] {elapsed:.2f}s",
        title="📈 Final Summary",
        border_style="green" if failed == 0 else "yellow"
    )
    console.print(summary)
    
    # Generate report file
    report_file = f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("CARANGOS S/A - TEST REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Test Suites: {total}\n")
        f.write(f"Passed: {passed}\n")
        f.write(f"Failed: {failed}\n")
        f.write(f"Success Rate: {(passed/total*100):.1f}%\n")
        f.write(f"Time Elapsed: {elapsed:.2f}s\n\n")
        f.write("=" * 80 + "\n")
        f.write("DETAILED RESULTS\n")
        f.write("=" * 80 + "\n\n")
        
        for test_name, result in results.items():
            f.write(f"\n{test_name}\n")
            f.write("-" * 80 + "\n")
            f.write(f"Status: {'PASS' if result['success'] else 'FAIL'}\n")
            f.write(f"Output:\n{result['output']}\n")
    
    console.print(f"\n[cyan]📄 Report saved to: {report_file}[/cyan]")
    
    # Exit code
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ Tests interrupted by user[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]❌ Fatal error: {e}[/red]")
        import traceback
        console.print(traceback.format_exc())
        sys.exit(1)
