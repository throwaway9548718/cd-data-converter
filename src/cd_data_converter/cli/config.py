from cd_data_converter.core.file_handlers import generate_default_filename

inputfile = {
    "default": ...,
    "exists": True,
    "file_okay": True,
    "dir_okay": False,
    "readable": True,
    "resolve_path": True,
    "help": "An XML file with CD data to parse.",
}

outputfile = {
    "default": generate_default_filename,
    "help": "Name of the output JSON file.",
}
