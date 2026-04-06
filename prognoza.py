import requests

def nabavi_temperaturu(grad):
    # Simuliramo poziv pravog API-ja
    odgovor = requests.get(f"https://vreme.com/{grad}")
    podaci = odgovor.json()
    return podaci["temp"]
