from plugin_loader import load_plugins
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

def main():
    console.print(
        Panel.fit(
            "[bold red]🖤 X‑OSINT Framework v4[/bold red]\n[green]Military Edition[/green]",
            border_style="red"
        )
    )

    plugins = load_plugins()

    table = Table(title="Loaded Plugins", box=box.DOUBLE_EDGE)
    table.add_column("Plugin Name", style="cyan", justify="center")

    for plugin in plugins:
        table.add_row(plugin.__name__)

    console.print(table)

    for plugin in plugins:
        console.print(f"\n[bold yellow]Running {plugin.__name__}...[/bold yellow]")
        plugin.run()

if __name__ == "__main__":
    main()
