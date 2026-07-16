import os

import questionary
from rich.console import Console


NOTES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "notes")


def list_notes() -> list[str]:
    if not os.path.exists(NOTES_DIR):
        return []
    return [f for f in os.listdir(NOTES_DIR) if f.endswith(".md")]


def select_note(console: Console) -> str | None:
    console.clear()
    console.print("[bold green]list of notes[/bold green] - stored in [bold cyan]notes/[/bold cyan]")

    note_files = list_notes()
    if not note_files:
        console.print("[yellow]no notes found.[/yellow]")
        return None

    question = questionary.select(
        "select action :",
        choices=note_files + ["go back"],
        instruction="(use arrow keys)",
    ).ask()

    if question is None or question == "go back":
        return None

    return os.path.join(NOTES_DIR, question)
