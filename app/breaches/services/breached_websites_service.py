import requests


def breached_websites():
    response = requests.get("https://haveibeenpwned.com/api/v3/breaches")
    if response.status_code != 200:
        return ""
    return response.json()
