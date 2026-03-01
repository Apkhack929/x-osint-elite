import socket
from rich.console import Console

console = Console()

def run():
    domain = input("Enter domain: ")
    try:
        ip = socket.gethostbyname(domain)
        console.print(f"[green][+] Domain IP:[/green] {ip}")
    except:
        console.print("[red][-] Could not resolve domain[/red]")
