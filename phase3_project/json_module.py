import json
from typing import TextIO


def json_export(kwargs: dict):
    return json.dump(kwargs, open('json_file.json', 'w'))

def json_import(file: TextIO):
    return json.load(file)

