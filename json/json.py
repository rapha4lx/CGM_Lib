import json
import os


def load_json(path='emails.json'):
    if not os.path.exists(path):
        return None

    with open(path, 'r', encoding='utf-8') as file:
        emails_data = json.load(file)
        return emails_data