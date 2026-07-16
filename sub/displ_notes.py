import os

import questionary
from rich.console import Console
from rich.panel import Panel

from sub import select_note
from sub.editor import BreakableMarkdown


console = Console()


def displayNotes():
    console.clear()
    filepath = select_note(console)
    if filepath is None:
        return

    with open(filepath, "r") as f:
        content = f.read()

    console.clear()
    console.print(Panel(BreakableMarkdown(content), title=os.path.basename(filepath), border_style="green"))

    questionary.select(
        "select action :",
        choices=["go back"],
        instruction="(use arrow keys)",
    ).ask()
