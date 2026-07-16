# questionary - markdown note taking system
# @procopioos

import questionary
from rich.console import Console

import sub.displ_notes as displayNotes
import sub.new_note as NewNote
import sub.edit_note as editNote
import sub.delete_notes as deleteNote
import sub.about as AboutMenu

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

def delete_note():
    deleteNote.deleteNote()
    pass

def openAbout():
    AboutMenu.about_section()
    pass

def displ_menu():
    while True:
        console.clear()
        console.print("   ▄▄ █    ▄   ▄███▄     ▄▄▄▄▄      ▄▄▄▄▀ ▄█ ████▄    ▄   ██   █▄▄▄▄ ▀▄    ▄ ")
        console.print("  █   █     █  █▀   ▀   █     ▀▄ ▀▀▀ █    ██ █   █     █  █ █  █  ▄▀   █  █  ")
        console.print("  ▀▀▀█  █   █ ██▄▄   ▄  ▀▀▀▀▄       █    ██ █   █ ██   █ █▄▄█ █▀▀▌     ▀█    ")
        console.print("     █  █   █ █▄   ▄▀ ▀▄▄▄▄▀       █     ▐█ ▀████ █ █  █ █  █ █  █     █    ")
        console.print("      █ █▄ ▄█ ▀███▀               ▀       ▐       █  █ █    █   █    ▄▀      ")
        console.print("       ▀ ▀▀▀                                      █   ██   █   ▀            ")
        console.print("                                                          ▀                 ")

        console.print("[bold green]questionary[/bold green] - markdown note taking system [yellow]v0.1.2[/yellow]\n")

        ACTIONS = {
            "display notes": lambda: displ_notes(),
            "add note": lambda: new_note(),
            "edit note": lambda: edit_note(),
            "delete note": lambda: delete_note(),
            "about": lambda: openAbout(),
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