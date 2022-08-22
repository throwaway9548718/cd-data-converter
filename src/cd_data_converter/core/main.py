import json
from pathlib import Path

from cd_data_converter.assets.countries import known_countries
from cd_data_converter.core.file_handlers import file_reader, file_writer
from cd_data_converter.core.parser_ import Parser
from cd_data_converter.utils.logger import logger


def main(input_file: Path, output_file: str) -> None:
    raw_data = file_reader(input_file)
    parsed_data = Parser(logger, known_countries).parse_cd_catalog(raw_data)
    file_writer(output_file, json.dumps(parsed_data))
