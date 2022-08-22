from pathlib import Path

import typer

from cd_data_converter.cli import config
from cd_data_converter.core.main import main


def app(
    inputfile: Path = typer.Argument(**config.inputfile),  # type: ignore[arg-type]
    outputfile: str = typer.Argument(**config.outputfile),  # type: ignore[arg-type]
) -> None:
    """
    Parse XML files with CD data to JSON.
    """
    return main(inputfile, outputfile)


def run() -> None:
    typer.run(app)


if __name__ == "__main__":
    run()
