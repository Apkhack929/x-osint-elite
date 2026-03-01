import requests
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def run():
    username = input("Enter username to scan: ")

    sites = {
        "GitHub": "https://github.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Google Profile": "https://profiles.google.com/{}",
        "Yahoo Profile": "https://profile.yahoo.com/{}"
    }

    table = Table(title="Username Scan Results", box=box.ROUNDED)
    table.add_column("Platform", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("URL", style="green")

    for site, url in sites.items():
        full_url = url.format(username)
        try:
            r = requests.get(full_url, timeout=5)
            if r.status_code == 200:
                table.add_row(site, "[green]FOUND[/green]", full_url)
            else:
                table.add_row(site, "[red]NOT FOUND[/red]", "-")
        except:
            table.add_row(site, "[yellow]ERROR[/yellow]", "-")

    console.print(table)
