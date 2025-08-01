import json
import os


def load_emails(path='emails.json'):
    if not os.path.exists('emails.json'):
        raise FileNotFoundError(f"File not found: {path}")

    with open('emails.json', 'r', encoding='utf-8') as file:
        emails_data = json.load(file)
        #emails_data = emails_data.get("default", [])
        return emails_data