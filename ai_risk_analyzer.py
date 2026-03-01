from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, SpinnerColumn, TextColumn
from rich import box
import random
import time

console = Console()
plugin.run () pluging.ai_risk_analayzer
def run():
    console.print(Panel.fit("[bold blue]AI Risk Analyzer[/bold blue]", border_style="blue"))
    
    username = input("Enter username to analyze risk: ")

    console.print(f"[yellow]Analyzing {username}...[/yellow]\n")

    # Simulate AI Risk Score calculation
    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
        BarColumn(bar_width=None),
        "[progress.percentage]{task.percentage:>3.0f}%",
        console=console
    ) as progress:

        task = progress.add_task("Calculating Risk Score", total=100)
        for i in range(0, 101, 10):
            time.sleep(0.1)
            progress.update(task, advance=10)

    # Generate a simulated Risk Score
    score = random.randint(0, 100)

    # Color based on score
    if score < 30:
        color = "green"
        level = "LOW"
    elif score < 70:
        color = "yellow"
        level = "MEDIUM"
    else:
        color = "red"
        level = "HIGH"

    console.print(Panel.fit(f"Risk Score: [bold {color}]{score}[/bold {color}] ({level})", border_style=color))
