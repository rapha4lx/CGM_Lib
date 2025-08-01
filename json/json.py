import json
import os


def load_json(path='emails.json'):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, 'r', encoding='utf-8') as file:
        emails_data = json.load(file)
        #emails_data = emails_data.get("default", [])
        return emails_data