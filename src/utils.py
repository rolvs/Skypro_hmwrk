import json


def load_operations(path: str) -> list[dict]:
    """
    Reads financial operations from a JSON file.

    Returns an empty list if the file is not found,
    empty, or does not contain a list.
    """
    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
