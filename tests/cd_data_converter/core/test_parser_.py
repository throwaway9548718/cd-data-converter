import json
from pathlib import Path

from src.cd_data_converter.assets.countries import known_countries
from src.cd_data_converter.core.file_handlers import file_reader
from src.cd_data_converter.core.parser_ import Parser
from src.cd_data_converter.utils.logger import logger

current_file = str(Path(__file__).parent.resolve())


def test_parse_cd_catalog():
    parser = Parser(logger, known_countries)
    data = file_reader(current_file + "/../test_assets/cd_catalog.xml")
    expected_data = json.loads(file_reader(current_file + "/../test_assets/cd_catalog.json"))
    parsed_data = parser.parse_cd_catalog(data)
    assert parsed_data == expected_data


def test_parser_logs_duplicates(caplog):
    parser = Parser(logger, known_countries)
    data = file_reader(current_file + "/../test_assets/cd_catalog_duplicate.xml")
    expected_data = json.loads(file_reader(current_file + "/../test_assets/cd_catalog.json"))
    parsed_data = parser.parse_cd_catalog(data)
    assert parsed_data == expected_data
    assert "Filtered out duplicate:" in caplog.text


def test_parser_logs_broken_file(caplog):
    parser = Parser(logger, known_countries)
    data = file_reader(current_file + "/../test_assets/cd_catalog_broken_tag.xml")
    parser.parse_cd_catalog(data)
    assert "Failed to parse XML file: " in caplog.text


def test_parser_logs_missing_data(caplog):
    parser = Parser(logger, known_countries)
    data = file_reader(current_file + "/../test_assets/cd_catalog_missing_data.xml")
    parser.parse_cd_catalog(data)
    assert "Failed to parse item" in caplog.text
