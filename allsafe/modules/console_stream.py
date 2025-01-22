from rich.console import Console
from rich.prompt import Prompt
from rich.status import Status
from rich.panel import Panel


class Style:
    RED = "#cc3333"
    GREEN = "#00a693"
    GRAY = "#6c757d"
    PASSWD = f"bold {GREEN}"

    def __getattr__(self, name):
        def _get_md(text: str) -> str:
            color = getattr(self, name.upper())
            return self.get_md(color, text)

        return _get_md

    def get_md(self, color, text):
        return f"[{color}]{text}[/{color}]"  # [color]text[/color]


class ConsoleStream:
    def __init__(self) -> None:
        self.writer = Console()
        self.styles = Style()

    def panel(self, title, text, **kwargs):
        panel = Panel.fit(text, title=title, **kwargs)
        self.write(panel, justify="left")

    def ask(self, prompt, **kwargs):
        style = kwargs.pop("style", None)
        if style is not None:  # might be needed in the future
            prompt = self.styles.get_md(style, prompt)
        result = ""
        while not result:
            result = Prompt.ask(prompt, console=self.writer, **kwargs)
            if kwargs.get("default", None) is not None:
                break
        return result

    def write(self, text, **kwargs):
        self.writer.print(text, **kwargs)

    def status(self, status, **kwargs):
        return Status(status, console=self.writer, **kwargs)
