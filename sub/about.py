import questionary
from rich.console import Console
from rich.panel import Panel

console = Console()
def about_section():
    console.clear()
    
    about_content = """
[bold green]questionary[/bold green] - markdown note taking system

a simple terminal-based note-taking application built with Python.

version [yellow]0.1.3[/yellow]

features:
• create new markdown notes
• view rendered markdown in the terminal
• edit existing notes with live preview
• single newlines render as line breaks

created by [bold cyan]@procopioos[/bold cyan]
"""

    contact_info = """
    [bold green]contact info[/bold green]
    • GitHub: [cyan]https://github.com/procopioos[/cyan]
    • Email: [cyan]procopiosimone9@gmail.com[/cyan]
    """

    about_panel = Panel(
        about_content,
        title="about",
        border_style="green",
        padding=(1, 2)
    )
    
    console.print(about_panel)
    
    choice = questionary.select(
        "select action :",
        choices=["contact info", "go back"],
        instruction="(use arrow keys)",
    ).ask()

    if choice == "contact info":
        contact_panel = Panel(
            contact_info,
            title="contact info",
            border_style="green",
            padding=(1, 2)
        )
        console.clear()
        console.print(contact_panel)

        choice = questionary.select(
            "select action :",
            choices=["go back"],
            instruction="(use arrow keys)",
        ).ask()
    