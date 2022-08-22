from datetime import datetime
from pathlib import Path


def file_reader(path: Path) -> str:
    with open(path, "r") as file:
        return file.read()


def file_writer(file_name: str, file_content: str) -> int:
    with open(file_name, "w") as file:
        return file.write(file_content)


def generate_default_filename() -> str:
    return f"cd-data-converter-export-{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
