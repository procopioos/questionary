import os
import re

import questionary
from rich.console import Console

from sub import NOTES_DIR
from sub.editor import create_editor


console = Console()


def newNote():
    console.clear()
    console.print("[bold green]new note[/bold green]")

    title = questionary.text("note title:").ask()
    if not title:
        console.print("[red]no title provided, cancelled.[/red]")
        return

    safe_name = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
    if not safe_name:
        console.print("[red]invalid title, cancelled.[/red]")
        return

    os.makedirs(NOTES_DIR, exist_ok=True)

    filepath = os.path.join(NOTES_DIR, f"{safe_name}.md")

    if os.path.exists(filepath):
        overwrite = questionary.confirm(f"{safe_name}.md already exists. overwrite?").ask()
        if not overwrite:
            console.print("[yellow]cancelled.[/yellow]")
            return

    create_editor(filepath)

    console.print(f"[bold green]note saved:[/bold green] notes/{safe_name}.md")
