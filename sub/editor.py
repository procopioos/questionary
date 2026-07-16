import os
from io import StringIO

from markdown_it import MarkdownIt
from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.document import Document
from prompt_toolkit.layout import Layout, HSplit, Window
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


class BreakableMarkdown(Markdown):


    def __init__(self, markup: str, **kwargs):
        super().__init__(markup, **kwargs)
        parser = MarkdownIt().enable("strikethrough").enable("table")
        parser.options["breaks"] = True
        self.parsed = parser.parse(markup)
        for token in self.parsed:
            if token.children:
                for child in token.children:
                    if child.type == "softbreak" and child.tag == "br":
                        child.type = "hardbreak"


def create_editor(filepath: str):
    console = Console()
    width, height = console.size
    panel_height = height - 1
    filename = os.path.basename(filepath)

    status_message = ""

    def get_display():
        text = editor_buffer.text or "_start typing..._"
        buf = StringIO()
        inner_console = Console(file=buf, width=width, force_terminal=True)
        md = BreakableMarkdown(text)
        panel = Panel(md, title=filename, border_style="green", height=panel_height, title_align="left")
        inner_console.print(panel)
        return ANSI(buf.getvalue())

    def get_status():
        if status_message:
            return status_message
        doc = editor_buffer.document
        line = doc.cursor_position_row + 1
        col = doc.cursor_position_col + 1
        return f"line {line}: column {col}  |  ctrl+x: save & exit"

    def on_text_changed(_buf=None):
        nonlocal status_message
        status_message = ""
        display_control.text = get_display()
        status_control.text = get_status()
        app.invalidate()

    initial_text = ""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            initial_text = f.read()

    editor_buffer = Buffer(
        multiline=True,
        on_text_changed=on_text_changed,
        on_cursor_position_changed=on_text_changed,
        document=Document(initial_text),
    )
    display_control = FormattedTextControl(get_display)
    status_control = FormattedTextControl(get_status)

    layout = Layout(
        HSplit([
            Window(display_control, height=height - 2),
            Window(status_control, height=1),
            Window(BufferControl(editor_buffer), height=1),
        ])
    )

    kb = KeyBindings()

    @kb.add('c-x')
    def save_and_exit(_event):
        nonlocal status_message
        content = editor_buffer.text.strip()
        if not content:
            status_message = "cannot save: document is empty"
            status_control.text = get_status()
            app.invalidate()
            return
        with open(filepath, "w") as f:
            f.write(editor_buffer.text)
        app.exit()

    app = Application(layout=layout, full_screen=True, key_bindings=kb)

    on_text_changed()
    app.run()


if __name__ == "__main__":
    create_editor("/tmp/test_note.md")
