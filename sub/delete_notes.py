import os
import questionary
from rich.console import Console
from sub import select_note


console = Console()

def deleteNote():
    console.clear()
    console.print("[bold red]questionary[/bold red] - delete a note from the repository")
    selected_note = select_note(console)
    if selected_note is None:
        console.print("[yellow]no note selected, cancelled.[/yellow]")
        return
    
    confirm = questionary.confirm(f"Are you sure you want to delete '{os.path.basename(selected_note)}'?").ask()
    if confirm:
        os.remove(selected_note)
        console.print(f"[bold green]note deleted:[/bold green] {os.path.basename(selected_note)}")

    pass