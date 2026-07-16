from rich.console import Console

import sub.editor as editor
from sub import select_note


def editNote():
    filepath = select_note(Console())
    if filepath is None:
        return

    editor.create_editor(filepath)
