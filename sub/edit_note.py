from rich.console import Console

import sub.editor as editor
from sub import select_note

console = Console()

def editNote():
    console.clear()
    filepath = select_note(console)
    if filepath is None:
        return

    editor.create_editor(filepath)
