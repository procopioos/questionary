# Questionary

A simple CLI note-taking system built with Python.

## Features

- Create new markdown notes
- View rendered markdown in the terminal
- Edit existing notes with live preview
- Single newlines render as line breaks

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

Use the menu to create, view, or edit notes. Notes are saved as `.md` files in the `notes/` directory.

## Dependencies

- [questionary](https://github.com/tmbo/questionary) - interactive prompts
- [rich](https://github.com/Textualize/rich) - terminal formatting and markdown rendering
- [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) - full-screen editor
