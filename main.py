import questionary
from rich.console import Console

import sub.displ_notes as displayNotes
import sub.new_note as NewNote
import sub.edit_note as editNote

console = Console()
console.clear()

def displ_notes():
    displayNotes.displayNotes()
    pass

def new_note():
    NewNote.newNote()
    pass

def edit_note():
    editNote.editNote()
    pass

def displ_menu():
    while True:
        console.clear()
        console.print("[bold green]markdown notes[/bold green] - simple note taking system")

        ACTIONS = {
            "display notes": lambda: displ_notes(),
            "add note": lambda: new_note(),
            "edit note": lambda: edit_note(),
            "delete note": lambda: console.print("you selected action 4"), # TODO: implement note deletion
            "exit": None,
        }

        question = questionary.select(
            "select action :",
            choices=list(ACTIONS.keys()),
            instruction="(use arrow keys)"
        ).ask()

        if question is None or question == "exit":
            console.clear()
            break

        ACTIONS[question]()

displ_menu()