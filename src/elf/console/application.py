import typer
import sys

# from typing import Optional

app = typer.Typer()


@app.command()
def dothings() -> None:
    """
    The entrypoint for the CLI
    """
    raise NotImplementedError


def main() -> int:
    """
    Call the application
    """
    try:
        app()
        return 0
    except Exception as e:
        print(e, file=sys.stderr)
        return 1
