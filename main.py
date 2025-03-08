from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def main():
    console.print(Panel("[bold blue]Main Menu[/bold blue]", expand=False))
    console.print("1. Option 1")
    console.print("2. Option 2")
    console.print("3. Option 3")

    choice = Prompt.ask("Choose an option", choices=["1", "2", "3"], default="1")

    if choice == "1":
        console.print("[green]You chose Option 1[/green]")
    elif choice == "2":
        console.print("[green]You chose Option 2[/green]")
    elif choice == "3":
        console.print("[green]You chose Option 3[/green]")

if __name__ == "__main__":
    main()
