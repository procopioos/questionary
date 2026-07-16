import questionary
from rich.console import Console

console = Console()
console.clear()

def repoLocation():
    console.clear()
    console.print("[bold green]questionary[/bold green] - change the location of the notes repository")
    # TODO: Implement the logic to change the notes repository location
    pass

def settingsMenu():
    while True:
        console.clear()
        console.print("[bold green]questionary[/bold green] - settings menu")

        ACTIONS = {
            "notes repo location": lambda: None,
            "go back": None,
        }

        question = questionary.select(
            "select action :",
            choices=list(ACTIONS.keys()),
            instruction="(use arrow keys)"
        ).ask()

        if question is None or question == "go back":
            console.clear()
            break

        ACTIONS[question]()