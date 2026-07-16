import questionary
from rich.console import Console
from rich.panel import Panel

console = Console()
def about_section():
    console.clear()
    
    about_content = """
[bold green]questionary[/bold green] - markdown note taking system

A simple terminal-based note-taking application built with Python.

Version [yellow]0.1.2[/yellow]

Features:
• Create new markdown notes
• View rendered markdown in the terminal
• Edit existing notes with live preview
• Single newlines render as line breaks

Created by [bold cyan]@procopioos[/bold cyan]
"""
    
    about_panel = Panel(
        about_content,
        title="about",
        border_style="green",
        padding=(1, 2)
    )
    
    console.print(about_panel)
    
    questionary.select(
        "select action :",
        choices=["go back"],
        instruction="(use arrow keys)",
    ).ask()
